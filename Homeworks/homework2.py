from datetime import datetime, timedelta


def filter_by_category(purchases, category):
    """
    Фильтрует покупки по указанной категории.
    :param purchases: список покупок
    :param category: категория для фильтрации
    :return: список покупок в указанной категории
    """
    
    return [purchase for purchase in purchases if purchase[3] == category]


def filter_recent_purchases(purchases, days):
    """
    Фильтрует покупки, сделанные за последние N дней.
    :param purchases: список покупок
    :param days: количество дней для фильтрации
    :return: список покупок за последние N дней
    """
    current_date = datetime.now()  
    date_limit = current_date - timedelta(days=days)  

 
    return [purchase for purchase in purchases if datetime.strptime(purchase[4], "%Y-%m-%d") >= date_limit]


def total_spent_by_client(purchases, callback):
    """
    Подсчитывает общую сумму покупок каждого клиента.
    :param purchases: список покупок
    :param callback: функция обработки результата
    :return: результат выполнения callback с данными по клиентам
    """
    client_totals = {}  
    for purchase in purchases:
        client_id = purchase[0]  
        amount = purchase[2]  
       
        client_totals[client_id] = client_totals.get(client_id, 0) + amount
    return callback(client_totals)  


def sort_purchases(purchases):
    """
    Сортирует покупки сначала по сумме (убывание), затем по категориям (алфавитный порядок).
    :param purchases: список покупок
    :return: отсортированный список покупок
    """
   
    return sorted(purchases, key=lambda x: (-x[2], x[3]))


def generate_report(purchases, client_id):
    """
    Генерирует отчет о покупках для указанного клиента.
    :param purchases: список покупок
    :param client_id: ID клиента
    :return: отчет в виде словаря
    """
    
    client_purchases = [purchase for purchase in purchases if purchase[0] == client_id]

    
    purchases_list = [{"product": purchase[1], "amount": purchase[2]} for purchase in client_purchases]

    
    total_spent = sum(purchase[2] for purchase in client_purchases)

   
    report = {
        "client_id": client_id,  
        "purchases": purchases_list,  
        "total_spent": total_spent  
    }
    return report

purchase_data = [
    [1, "Laptop", 1200, "electronics", "2024-12-01"],
    [2, "Phone", 800, "electronics", "2024-12-03"],
    [3, "Shoes", 100, "fashion", "2024-12-05"],
    [1, "Headphones", 200, "electronics", "2024-12-05"],
    [2, "Jacket", 150, "fashion", "2024-12-06"],
    [4, "Smartwatch", 300, "electronics", "2024-12-07"]
]


if __name__ == "__main__":
    
    print("Фильтрация по категории 'electronics':")
    print(filter_by_category(purchase_data, "electronics"))

    
    print("\nФильтрация покупок за последние 3 дня:")
    print(filter_recent_purchases(purchase_data, 3))

   
    print("\nОбщая сумма покупок каждого клиента:")
    print(total_spent_by_client(purchase_data, lambda x: x))

    
    print("\nСортировка покупок по сумме и категориям:")
    print(sort_purchases(purchase_data))

    
    print("\nОтчет для клиента с ID = 1:")
    print(generate_report(purchase_data, 1))