from src.classes_description import Product, Category


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
    assert Category.category_count == 1
    assert Category.product_count == 2  # 2 products in the category


def test_product_creation():
    product = Product("Product 1", "Product 1", 80, 15)
    assert product.name == "Product 1"
    assert product.description == "Product 1"
    assert product.price == 80
    assert product.quantity == 15


def test_set_price_zero():
    product = Product("Product 1", "Product 1", 80, 15)
    product.price = 0


def test_category_products_str():
    products = [
        Product("Product 1", "Test product 1", 10.0, 2),
        Product("Product 2", "Test product 2", 20.0, 3)
    ]
    category = Category("Test Category", "This is a test category", products)

    product_strs = category.products.split('\n')
    assert len(product_strs) == 2  # There should be two products listed
    assert product_strs[0] == "Product 1, 10.0 руб. Остаток: 2 шт."
    assert product_strs[1] == "Product 2, 20.0 руб. Остаток: 3 шт."


def test_category_adding_product():
    products = [
        Product("Product 1", "Description 1", 10.0, 2),
    ]
    category = Category("Test Category", "This is a test category", products)

    new_product = Product("Product 2", "Description 2", 15.0, 3)
    category.add_product(new_product)

    assert category.__str__() == "Test Category, общее количество продуктов: 5 шт."  # 2 + 3 = 5