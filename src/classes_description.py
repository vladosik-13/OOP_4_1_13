class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, new_product: dict):
        name = new_product.get("name")
        description = new_product.get("description")
        price = new_product.get("price")
        quantity = new_product.get("quantity")
        return Product(name, description, price, quantity)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            if type(self) == type(other):
                return (self.price * self.quantity) + (other.price * other.quantity)
            else:
                raise TypeError(
                    f"Невозможно сложить товар типа {type(self).__name__} с товаром типа {type(other).__name__}.")
        return NotImplemented


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Добавляемый объект должен быть продуктом или его наследником.")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        return "\n".join(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
                         for product in self.__products)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, общее количество продуктов: {total_quantity} шт."


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        return (super().__str__() + f", Эффективность: {self.efficiency}, Модель: {self.model}, "
                f"Встроенная память: {self.memory} ГБ, Цвет: {self.color}")


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        return (super().__str__() + f", Страна производства: {self.country}, Срок прорастания: {self.germination_period} дней, "
                f"Цвет: {self.color}")
