# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: product.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rproduct.proto\x12\x07product\"\\\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x01\x12\x13\n\x0b\x63\x61tegory_id\x18\x05 \x01(\x05\"$\n\x08\x43\x61tegory\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"6\n\x11\x41\x64\x64ProductRequest\x12!\n\x07product\x18\x01 \x01(\x0b\x32\x10.product.Product\" \n\x12\x41\x64\x64ProductResponse\x12\n\n\x02id\x18\x01 \x01(\x05\"9\n\x12\x41\x64\x64\x43\x61tegoryRequest\x12#\n\x08\x63\x61tegory\x18\x01 \x01(\x0b\x32\x11.product.Category\"!\n\x13\x41\x64\x64\x43\x61tegoryResponse\x12\n\n\x02id\x18\x01 \x01(\x05\"\"\n\x14\x44\x65leteProductRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"(\n\x15\x44\x65leteProductResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xf1\x01\n\x0eProductService\x12\x45\n\nAddProduct\x12\x1a.product.AddProductRequest\x1a\x1b.product.AddProductResponse\x12H\n\x0b\x41\x64\x64\x43\x61tegory\x12\x1b.product.AddCategoryRequest\x1a\x1c.product.AddCategoryResponse\x12N\n\rDeleteProduct\x12\x1d.product.DeleteProductRequest\x1a\x1e.product.DeleteProductResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'product_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PRODUCT._serialized_start=26
  _PRODUCT._serialized_end=118
  _CATEGORY._serialized_start=120
  _CATEGORY._serialized_end=156
  _ADDPRODUCTREQUEST._serialized_start=158
  _ADDPRODUCTREQUEST._serialized_end=212
  _ADDPRODUCTRESPONSE._serialized_start=214
  _ADDPRODUCTRESPONSE._serialized_end=246
  _ADDCATEGORYREQUEST._serialized_start=248
  _ADDCATEGORYREQUEST._serialized_end=305
  _ADDCATEGORYRESPONSE._serialized_start=307
  _ADDCATEGORYRESPONSE._serialized_end=340
  _DELETEPRODUCTREQUEST._serialized_start=342
  _DELETEPRODUCTREQUEST._serialized_end=376
  _DELETEPRODUCTRESPONSE._serialized_start=378
  _DELETEPRODUCTRESPONSE._serialized_end=418
  _PRODUCTSERVICE._serialized_start=421
  _PRODUCTSERVICE._serialized_end=662
# @@protoc_insertion_point(module_scope)
