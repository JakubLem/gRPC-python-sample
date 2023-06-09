# gRPC Python Example with SQLAlchemy and Faker

This repository contains an example of a gRPC server and client implemented in Python. The example demonstrates how to define a simple product service with operations to add and delete products. It uses SQLAlchemy with SQLite for data storage and the Faker library for generating random product data.

## Features

- gRPC server and client implementation in Python
- Product service definition using Protocol Buffers
- Add and delete products
- SQLAlchemy with SQLite for data storage
- Faker library for generating random product data
- Positive and negative testing using pytest
- Code quality checks using pylama
- Validation for adding products (price and name length constraints)

## Learning gRPC

This repository also includes a comprehensive learning guide for gRPC in the `LEARN.md` file. This guide covers essential topics and concepts that you should familiarize yourself with when starting to work with gRPC. Refer to this file for a solid foundation in gRPC and to gain a better understanding of the technologies used in this example project.

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

## Code Quality and GitHub Actions

This project uses GitHub Actions for continuous integration. The repository includes a GitHub Actions workflow that runs Pylama, a code quality tool for Python, to ensure that the code adheres to best practices and coding standards.

The Pylama configuration is stored in the `pylama.ini` file, which allows you to customize the code quality checks according to your preferences.

To run Pylama locally, run the following command:

```bash
pylama
```

## Testing
To run tests for the project, navigate to the shopApp directory and use the pytest command with the -x and -vv flags:

```bash
cd shopApp/
pytest -x -vv
```

The -x flag stops the testing process after the first failure, while the -vv flag increases verbosity to provide more detailed test output. This allows you to efficiently test the application and identify any issues or failures.
