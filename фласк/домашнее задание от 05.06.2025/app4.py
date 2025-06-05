from flask import Flask, render_template, request
from datetime import datetime

# Создаем экземпляр 
app = Flask(__name__)

# Функция для определения даты Дня программиста
def get_programmer_day(year):
    # Проверяем, является ли год високосным
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        # Високосный год: День программиста - 12 сентября
        return datetime(year, 9, 12)
    else:
        # Обычный год: День программиста - 13 сентября
        return datetime(year, 9, 13)

# Определяем маршрут для главной страницы
@app.route('/', methods=['GET', 'POST'])
def index():
    # Переменная для хранения результата
    result = None
    
    # Проверяем, был ли запрос методом POST (т.е. форма была отправлена)
    if request.method == 'POST':
        # Получаем год из формы и преобразуем его в целое число
        year = int(request.form['year'])
        
        # Получаем дату Дня программиста для указанного года
        programmer_day = get_programmer_day(year)
        
        # Форматируем дату и день недели для отображения
        result = programmer_day.strftime("%d %B (%A)").capitalize()  # Приводим к нужному формату

    # Возвращаем HTML-шаблон с переданным результатом
    return render_template('index4.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)  
