# Задание 1: Работа с многопоточностью (Threading)

# Описание: Вам необходимо разработать программу на Python,которая имитирует работу системы учета остатков товаров на
# складе. У вас есть общий ресурс — словарь, представляющийсобой склад, где ключи — это названия товаров (строки), а
# значения — их текущее количество (целые числа).

# Программа должна создать несколько потоков (например, 5-10).Каждый поток будет имитировать либо "поступление товара"
# (увеличение количества случайного товара на случайную величину), либо "отгрузку товара" (уменьшение количества
# случайного товара на случайную величину). Каждый поток должен выполнить определенное количество операций (например, 20-50).

# Требования
# - Создайте словарь, представляющий склад, с несколькими начальными товарами и их количествами
#  - Реализуйте две функции: add_item(stock, item_name, quantity) иremove_item(stock, item_name, quantity)
# - Создайте функцию, которую будут выполнять потоки. Эта функция должна случайным образом выбирать товар и
# операцию (добавление или удаление), а затем вызывать соответствующую функцию (add_item или remove_item).
# -Убедитесь, что количество товара не может стать отрицательным при отгрузке/
#  - Запустите несколько потоков, каждый из которых выполняет вашу функцию с операциями
# После завершения работы всех потоков выведите итоговое состояние склада.

import threading
import time
import random

stock = {
    "item1": 50,
    "item2": 30,
    "item3": 250,
    "item4": 130
}

stock_lock = threading.Lock()

def add_item(stock, item_name, quantity):
    with stock_lock:
        if item_name in stock:
            stock[item_name] += quantity
        else:
             stock[item_name] = quantity
        print(f'Добавлено {quantity} единиц товара {item_name}, новое количество: {stock[item_name]}')  

def remove_item(stock, item_name, quantity):
    with stock_lock:
        if item_name in stock and stock[item_name] >= quantity:
            stock[item_name] -= quantity  
            print(f'удалено {quantity} единиц товара {item_name}, новое количество: {stock[item_name]}')
        else:
            print(f'Не удалось удалить {quantity} единиц товара {item_name}. Недостаточно на складе.')

def thread_operation(stock): 
    for _ in range(random.randint(20, 50)):
        operation = random.choice(["add", "remove"]) 
        item_name = random.choice(list(stock.keys()))   
        quantity = random.randint(1, 10)    

        if operation == "add":
            add_item(stock, item_name, quantity)
        else:
            remove_item(stock, item_name, quantity) 
        time.sleep(random.uniform(0.1, 0.5))    


threads = []

for _ in range(random.randint(20, 50)):
    thread = threading.Thread(target=thread_operation, args=(stock,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("\nИтоговое количество товаров на складе: ")    
for item, quantity in stock.items():
    print(f"{item}: {quantity}")    







# Задание 2: Работа с многопроцессностью (Multiprocessing)

# Описание: Вам необходимо разработать программу на Python,которая выполняет computationally intensive задачу — вычисление
# факториала большого числа — параллельно, используя несколько процессов.

# Программа должна принимать на вход список чисел, для каждого из которых необходимо вычислить факториал. Вместо того чтобы 
# вычислять факториалы последовательно в одном процессе, вы должны распределить эту работу между несколькими процессами для ускорения выполнения.

# Требования
# - Реализуйте функцию calculate_factorial(n) которая принимает целое число n и возвращает его факториал. Используйте
# алгоритм, который может занять заметное время для больших n (например, простой цикл умножения)
# - Создайте список чисел, для которых нужно вычислить факториал (например, числа от 1000 до 1050)
# - Используя модуль multiprocessing, создайте пул процессов (Pool). Определите количество процессов, которое будет
# использоваться (например, по количеству ядер вашего процессора или фиксированное число)
# - Распределите вычисление факториалов для каждого числа из списка между процессами в пуле
# - Соберите результаты вычислений из всех процессовk6 Измерьте время выполнения программы с использованием
# многопроцессности. Для сравнения, можете также измерить время выполнения последовательного вычисления факториалов без использования многопроцессности.    


import time
import multiprocessing 

def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        print(i)
        print(result)
        result *= i
        
    return result

def factorials_in_parallel(numbers):
    with  multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(calculate_factorial, numbers)   
    return results

if __name__ == '__main__':
    numbers = list(range(1, 10))
    start_time = time.time()
    results_parallel = factorials_in_parallel(numbers)
    end_time = time.time()
    parallel_time = end_time - start_time

    print(f"Время выполнения с многозадачностью: {parallel_time:.4f} секунд")

    start_time = time.time()
    results_seq = [calculate_factorial(n) for n in numbers]
    end_time = time.time()
    seq_time = end_time - start_time

    print(f"Время выполнения без многозадачности: {seq_time:.4f} секунд")

    print(f"Первые 5 результатов с многозадачностью: {results_parallel[:5]}")
    print(f"Первые 5 результатов без многозадачности: {results_seq[:5]}")
