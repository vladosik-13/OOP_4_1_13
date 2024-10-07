import pytest
from src.classes_description import Product, Category, LawnGrass, Smartphone
from unittest.mock import patch


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

    assert category.__str__() == "Test Category, общее количество продуктов: 5 шт."


def test_smartphone_initialization():
    smartphone = Smartphone("iPhone 14", "Смартфон от Apple", 79999, 10, "A15 Bionic", "iPhone 14", 128, "синий")
    assert smartphone.name == "iPhone 14"
    assert smartphone.description == "Смартфон от Apple"
    assert smartphone.price == 79999
    assert smartphone.quantity == 10
    assert smartphone.efficiency == "A15 Bionic"
    assert smartphone.model == "iPhone 14"
    assert smartphone.memory == 128
    assert smartphone.color == "синий"


def test_lawn_grass_initialization():
    lawn_grass = LawnGrass("Газонная трава", "Трава для газона", 300, 50, "Россия", 14, "зеленый")
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Трава для газона"
    assert lawn_grass.price == 300
    assert lawn_grass.quantity == 50
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == 14
    assert lawn_grass.color == "зеленый"


def test_mixin_product_creation_output():
    with patch('builtins.print') as mocked_print:
        product = Product('Продукт1', 'Описание продукта', 1200, 10)

    mocked_print.assert_called_once_with("Создан объект класса Product с параметрами: "
                                         "'Продукт1', 'Описание продукта', 1200, 10")


def test_product_creation_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен."):
        Product(name="Тестовый продукт", description="Описание продукта", price=100.0, quantity=0)
