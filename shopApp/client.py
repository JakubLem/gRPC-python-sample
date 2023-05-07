import grpc
import product_pb2
import product_pb2_grpc
from faker import Faker


fake = Faker()


def add_product(stub, name, description, price):
    product = product_pb2.Product(name=name, description=description, price=price)
    request = product_pb2.AddProductRequest(product=product)
    response = stub.AddProduct(request)
    print(f"Added product with ID: {response.id}")


def delete_product(stub, product_id):
    request = product_pb2.DeleteProductRequest(id=product_id)
    response = stub.DeleteProduct(request)
    if response.success:
        print(f"Deleted product with ID: {product_id}")
    else:
        print(f"Product with ID: {product_id} not found")


def register_user(stub, username, email, password):
    response = stub.RegisterUser(
        product_pb2.RegisterUserRequest(username=username, email=email, password=password)
    )
    print(f"Registered user with ID: {response.id}")


def authenticate_user(stub, username, password):
    response = stub.AuthenticateUser(
        product_pb2.AuthenticateUserRequest(username=username, password=password)
    )
    print(f"Received authentication token: {response.token}")
    return response.token


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = product_pb2_grpc.ProductServiceStub(channel)

        # Add a random product
        name = fake.name()
        description = fake.text()
        price = fake.random_number(digits=2, fix_len=True)
        add_product(stub, name, description, price)


if __name__ == '__main__':
    run()
