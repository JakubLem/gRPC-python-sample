from models import User

import grpc
from concurrent import futures
import product_pb2
import product_pb2_grpc
from models import Product, Category, Session
from validators import validate_product_data
from auth import generate_token


class ProductService(product_pb2_grpc.ProductServiceServicer):
    def AddCategory(self, request, context):
        category_data = request.category
        new_category = Category(name=category_data.name)

        session = Session()
        session.add(new_category)
        session.commit()
        category_id = new_category.id
        session.close()

        return product_pb2.AddCategoryResponse(id=category_id)

    def AddProduct(self, request, context):
        print("add Project")
        product_data = request.product

        session = Session()
        try:
            validate_product_data(product_data, session)
        except ValueError as e:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))
        category = session.query(Category).filter_by(id=product_data.category_id).first()

        new_product = Product(
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
            category_id=category.id
        )

        session.add(new_product)
        session.commit()
        product_id = new_product.id
        session.close()

        return product_pb2.AddProductResponse(id=product_id)

    def DeleteProduct(self, request, context):
        print("delete Product")
        product_id = request.id
        
        session = Session()
        product = session.query(Product).filter_by(id=product_id).first()
        if product:
            session.delete(product)
            session.commit()
            session.close()
            return product_pb2.DeleteProductResponse(success=True)
        else:
            session.close()
            return product_pb2.DeleteProductResponse(success=False)

    def get_product_by_id(self, product_id):
        session = Session()
        product = session.query(Product).filter(Product.id == product_id).one_or_none()
        session.close()
        return product

    def get_category_by_id(self, category_id):
        session = Session()
        category = session.query(Category).filter(Category.id == category_id).one_or_none()
        session.close()
        return category
    
class UserService(product_pb2_grpc.UserServiceServicer):
    def RegisterUser(self, request, context):
        username = request.username
        email = request.email
        password = request.password

        session = Session()
        existing_user = session.query(User).filter(
            (User.username == username) | (User.email == email)
        ).first()

        if existing_user:
            context.abort(grpc.StatusCode.ALREADY_EXISTS, "User already exists")

        new_user = User(username=username, email=email)
        new_user.set_password(password)

        session.add(new_user)
        session.commit()
        user_id = new_user.id
        session.close()

        return product_pb2.RegisterUserResponse(id=user_id)

    def AuthenticateUser(self, request, context):
        username = request.username
        password = request.password

        session = Session()
        user = session.query(User).filter(User.username == username).first()
        session.close()

        if user and user.check_password(password):
            token = generate_token(user.id)
            return product_pb2.AuthenticateUserResponse(token=token)
        else:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid credentials")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(), server)
    product_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051.")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
