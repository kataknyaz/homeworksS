import logging
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List, Optional
from functools import wraps
import time

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Декоратор для логирования вызовов функций
def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'Вызов функции {func.__name__} с аргументами: {args}, {kwargs}')
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f'Функция {func.__name__} завершена за {end_time - start_time:.4f} секунд')
        return result
    return wrapper

# Класс товара
@dataclass
class Product:
    id: int
    name: str
    price: float
    quantity: int

# Абстрактный базовый класс для управления товарами
class AbstractProductManager(ABC):
    @abstractmethod
    def update_product(self, product: Product) -> None:
        pass

    @abstractmethod
    def calculate_discounted_price(self, product: Product, discount_percentage: float) -> float:
        pass

# Реализация менеджера товаров
class ProductManager(AbstractProductManager):
    def __init__(self):
        self.products: List[Product] = []

    @log_function_call
    def add_product(self, product: Product) -> None:
        self.products.append(product)
        logging.info(f'Добавлен товар: {product}')

    @log_function_call
    def update_product(self, product: Product) -> None:
        for idx, existing_product in enumerate(self.products):
            if existing_product.id == product.id:
                self.products[idx] = product
                logging.info(f'Обновлён товар: {product}')
                return
        logging.warning(f'Товар с ID {product.id} не найден для обновления.')

    @log_function_call
    def calculate_discounted_price(self, product: Product, discount_percentage: float) -> float:
        discounted_price = product.price * (1 - discount_percentage / 100)
        logging.info(f'Цена со скидкой для товара {product.name}: {discounted_price:.2f}')
        return discounted_price

    def list_products(self) -> List[Product]:
        return self.products


manager = ProductManager()

    # Добавление товаров
product1 = Product(id=1, name="Товар 1", price=100.0, quantity=10)
manager.add_product(product1)

product2 = Product(id=2, name="Товар 2", price=200.0, quantity=5)
manager.add_product(product2)

    # Обновление товара
updated_product1 = Product(id=1, name="Товар 1 обновлённый", price=90.0, quantity=15)
manager.update_product(updated_product1)

# Расчёт цены со скидкой
discounted_price = manager.calculate_discounted_price(updated_product1, 10)

# Список всех товаров
products = manager.list_products()
for prod in products:
    print(prod)
