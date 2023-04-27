import grpc
from concurrent import futures
import product_pb2
import product_pb2_grpc

# Import SQLAlchemy Product model and Session
from models import Product, Session

class ProductService(product_pb2_grpc.ProductServiceServicer):
    def AddProduct(self, request, context):
        print("add Project")
        product_data = request.product
        new_product = Product(
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
        )
        
        session = Session()
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

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()







