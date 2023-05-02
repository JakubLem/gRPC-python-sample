from models import Category


def validate_product_data(product_data, session):
    if product_data.price < 0:
        raise ValueError("Price cannot be negative")
    
    if len(product_data.name) > 20:
        raise ValueError("Product name cannot be longer than 20 characters")

    if not session.query(Category).filter_by(id=product_data.category_id).first():
        raise ValueError("Category not found")
