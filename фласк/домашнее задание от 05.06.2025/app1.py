from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Секретный ключ для использования flash сообщений

# Список пользователей (логин: пароль)
users = {
    'admin': 'admin123',
    'user': 'user123'
}

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']  # Получаем логин из формы
    password = request.form['password']  # Получаем пароль из формы

    # Проверка, есть ли пользователь в списке и правильный ли пароль
    if username in users and users[username] == password:
        flash(f'Добро пожаловать, {username}!', 'success')  # Успешное сообщение
        return redirect(url_for('home'))  # Перенаправляем на главную страницу
    else:
        flash('Неправильные логин или пароль.', 'error')  # Сообщение об ошибке
        return redirect(url_for('home'))  # Перенаправляем обратно на форму входа

if __name__ == '__main__':
    app.run(debug=True)  # Запускаем приложение в режиме отладки
