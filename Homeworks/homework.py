inventory = {
    101: {'name': 'Смартфон', 'category': 'Электроника', 'price': 29999, 'quantity': 50},
    102: {'name': 'Ноутбук', 'category': 'Электроника', 'price': 54999, 'quantity': 30},
    103: {'name': 'Кофеварка', 'category': 'Бытовая техника', 'price': 7999, 'quantity': 20},
}


def add_product(inventory, product_id, name, category, price, quantity):
    """
    Добавляет новый товар в инвентарь.
    Если товар с указанным product_id уже существует, увеличивает количество на складе.
    """
    if product_id in inventory:  
        inventory[product_id]["quantity"] += quantity  
    else:
        
        inventory[product_id] = {
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity
        }


def remove_product(inventory, product_id):
    """
    Удаляет товар из инвентаря по product_id.
    Если товар с таким product_id не существует, выводит сообщение об ошибке.
    """
    if product_id in inventory:  
        del inventory[product_id]  
    else:
        
        print(f"Ошибка: Товар с ID {product_id} не существует.")


def update_quantity(inventory, product_id, quantity):
    """
    Обновляет количество товара на складе.
    Если количество равно 0 или меньше, удаляет товар из инвентаря.
    """
    if product_id in inventory:  
        if quantity <= 0:
            
            del inventory[product_id]
        else:
           
            inventory[product_id]["quantity"] = quantity
    else:
        
        print(f"Ошибка: Товар с ID {product_id} не существует.")


def get_unique_categories(inventory):
    """
    Возвращает множество всех уникальных категорий товаров в инвентаре.
    """
    return {product["category"] for product in inventory.values()}

# Пример использования функций
# Добавляем новый товар
add_product(inventory, 104, "Телевизор", "Электроника", 45000, 15)
# Удаляем товар с ID 101
remove_product(inventory, 101)
# Обновляем количество товара с ID 102
update_quantity(inventory, 102, 25)
# Получаем список уникальных категорий
categories = get_unique_categories(inventory)
# Выводим категории
print(categories)