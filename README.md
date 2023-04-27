# gRPC Python Example with SQLAlchemy and Faker

This repository contains an example of a gRPC server and client implemented in Python. The example demonstrates how to define a simple product service with operations to add and delete products. It uses SQLAlchemy with SQLite for data storage and the Faker library for generating random product data.

## Features

- gRPC server and client implementation in Python
- Product service definition using Protocol Buffers
- Add and delete products
- SQLAlchemy with SQLite for data storage
- Faker library for generating random product data

## Installation

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Generate the gRPC Python files from the product.proto file:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. product.proto
```

## Usage (shopApp)

```bash
cd shopApp/
```  

1. Run the gRPC server:
```bash
python server.py
```

2. In a separate terminal, run the gRPC client to add a random product:

```bash
python client.py
```

## Repository Structure

### (shopApp):

- product.proto: Protocol Buffers file containing the product service definition
- product_pb2.py: Generated Python file containing messages defined in product.proto
- product_pb2_grpc.py: Generated Python file containing client and server classes for the product service
- server.py: Python script implementing the gRPC server
- client.py: Python script implementing the gRPC client
- models.py: SQLAlchemy model definition for the Product class and SQLite database setup


This README.md file provides an overview of the gRPC example, its features, installation instructions, usage, and the repository structure. You can include this content in your repository's README.md file to help users understand how to use your example project.
