import pytest
from main import Product, Category


def test_product_initialization():
    product = Product("Test Product", "This is a test product", 29.99, 5)
    assert product.name == "Test Product"
    assert product.description == "This is a test product"
    assert product.price == 29.99
    assert product.quantity == 5


def test_category_initialization():
    products = [Product("Product 1", "Test product 1", 10.0, 2),
                Product("Product 2", "Test product 2", 20.0, 3)]

    category = Category("Test Category", "This is a test category", products)

    assert category.name == "Test Category"
    assert category.description == "This is a test category"
    assert category.products == products
    assert Category.category_count == 1
    assert Category.product_count == 2  # 2 products in the category
