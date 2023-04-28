# validators.py
def validate_product_data(product_data):
    if product_data.price < 0:
        raise ValueError("Price cannot be negative")
    
    if len(product_data.name) > 20:
        raise ValueError("Product name cannot be longer than 20 characters")
