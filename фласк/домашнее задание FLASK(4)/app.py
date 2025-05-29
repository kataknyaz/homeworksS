import sqlite3
from flask import Flask, request, render_template, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Для использования flash-сообщений


def init_db():    # Функция для создания базы данных и таблицы
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER NOT NULL,
            registration_date TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Главная страница с формой
@app.route('/', methods=['GET'])
def home():
    return render_template('form.html')

# Обработка отправки формы
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']

    # Валидация данных
    if not (1 <= int(age) <= 120):
        flash('Возраст должен быть от 1 до 120 лет.')
        return redirect(url_for('home'))

    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email, age) VALUES (?, ?, ?)', (name, email, age))
        conn.commit()
        conn.close()
        flash('Пользователь успешно зарегистрирован!')
        return redirect(url_for('home'))
    except sqlite3.IntegrityError:
        flash('Пользователь с таким email уже существует.')
        return redirect(url_for('home'))

# Страница со списком пользователей
@app.route('/users', methods=['GET'])
def users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    user_list = cursor.fetchall()
    conn.close()
    return render_template('users.html', users=user_list)

if __name__ == '__main__':
    app.run(debug=True)



