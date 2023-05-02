import pytest
import product_pb2
import product_pb2_grpc
from server import ProductService
from grpc import insecure_channel
from concurrent import futures
import grpc

@pytest.fixture(scope="module")
def grpc_channel(grpc_server):
    return insecure_channel(grpc_server.insecure_address)

@pytest.fixture(scope="module")
def grpc_add_to_server():
    return product_pb2_grpc.add_ProductServiceServicer_to_server

@pytest.fixture(scope="module")
def grpc_servicer():
    return ProductService()

@pytest.fixture(scope="module")
def grpc_stub(grpc_add_to_server, grpc_servicer):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_add_to_server(grpc_servicer, server)
    port = server.add_insecure_port("[::]:0")
    server.start()

    with insecure_channel(f"localhost:{port}") as channel:
        yield product_pb2_grpc.ProductServiceStub(channel)

    server.stop(None)


def test_add_category(grpc_stub):
    # Call add_category and check if the new category is added
    new_category = product_pb2.Category(name="Test category")
    request = product_pb2.AddCategoryRequest(category=new_category)

    response = grpc_stub.AddCategory(request)
    added_category = ProductService().get_category_by_id(response.id)

    assert added_category is not None
    assert added_category.name == new_category.name


def test_add_product_with_invalid_category_id(grpc_stub):
    # Call add_product with an invalid category_id and check if an error is raised
    new_product = product_pb2.Product(name="Test product", description="Test description", price=100.0, category_id=9999)
    request = product_pb2.AddProductRequest(product=new_product)

    with pytest.raises(grpc.RpcError) as e:
        grpc_stub.AddProduct(request)

    assert e.value.code() == grpc.StatusCode.INVALID_ARGUMENT
    assert e.value.details() == "Category not found"


def test_add_product_with_valid_category_id(grpc_stub):
    # Call add_category to create a new category
    new_category = product_pb2.Category(name="Test category")
    category_request = product_pb2.AddCategoryRequest(category=new_category)
    category_response = grpc_stub.AddCategory(category_request)

    # Call add_product with the created category_id and check if the new product is added to the store
    new_product = product_pb2.Product(name="Test product", description="Test description", price=100.0, category_id=category_response.id)
    product_request = product_pb2.AddProductRequest(product=new_product)

    product_response = grpc_stub.AddProduct(product_request)
    added_product = ProductService().get_product_by_id(product_response.id)

    assert added_product is not None
    assert added_product.name == new_product.name
    assert added_product.description == new_product.description
    assert added_product.price == new_product.price
    assert added_product.category_id == new_product.category_id

def test_add_product_negative_price(grpc_stub):
    # Call add_product with a negative price and check if an error is raised
    new_product = product_pb2.Product(name="Test product", description="Test description", price=-5.0)
    request = product_pb2.AddProductRequest(product=new_product)

    with pytest.raises(grpc.RpcError) as e:
        grpc_stub.AddProduct(request)

    assert e.value.code() == grpc.StatusCode.INVALID_ARGUMENT
    assert e.value.details() == "Price cannot be negative"


def test_add_product_with_too_long_name(grpc_stub):
    # Call add_product with a too long name and check if an error is raised
    new_product = product_pb2.Product(name="Test product with a very long name", description="Test description", price=100.0)
    request = product_pb2.AddProductRequest(product=new_product)

    with pytest.raises(grpc.RpcError) as e:
        grpc_stub.AddProduct(request)

    assert e.value.code() == grpc.StatusCode.INVALID_ARGUMENT
    assert e.value.details() == "Product name cannot be longer than 20 characters"
