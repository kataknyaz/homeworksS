
from flask import Flask, render_template, request

# Создаем экземпляр 
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    # Переменная для хранения данных пользователя, если форма была отправлена
    user_data = None
    
    # Проверяем, был ли запрос методом POST (т.е. форма была отправлена)
    if request.method == 'POST':
        # Получаем данные из формы по именам полей
        first_name = request.form['first_name']  # Имя
        last_name = request.form['last_name']    # Фамилия
        age = request.form['age']                 # Возраст
        email = request.form['email']             # Email
        gender = request.form['gender']           # Пол
        address = request.form['address']         # Адрес для доставки
        
        # Проверяем, подписался ли пользователь на новости
        subscribe = 'subscribe' in request.form  # Если чекбокс был отмечен, то будет True, иначе False

        # Сохраняем данные в словаре user_data
        user_data = {
            'first_name': first_name,
            'last_name': last_name,
            'age': age,
            'email': email,
            'gender': gender,
            'address': address,
            'subscribe': subscribe
        }

    # Возвращаем HTML-шаблон с переданными данными пользователя
    return render_template('index3.html', user_data=user_data)

# Запускаем приложение, если файл выполняется как основная программа
if __name__ == '__main__':
    app.run(debug=True)  # Включаем режим отладки для автоматического перезапуска при изменениях
