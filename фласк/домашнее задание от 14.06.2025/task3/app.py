from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Секретный ключ для защиты сессий
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # URI для базы данных SQLite
db = SQLAlchemy(app)
login_manager = LoginManager(app)  # Инициализация менеджера логинов
login_manager.login_view = 'login'  # Указание маршрута для перенаправления при необходимости входа

# Модель пользователя
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

# Функция загрузки пользователя по ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Главная страница
@app.route('/')
def home():
    return render_template('home.html')  # Шаблон главной страницы

# Страница регистрации (просто для примера)
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Здесь должна быть логика для регистрации пользователя
    pass

# Страница входа
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:  # Проверка пароля (используйте хеширование в реальном приложении)
            login_user(user)  # Сохранение ID пользователя в сессии
            flash('Вы успешно вошли!', 'success')
            return redirect(url_for('protected'))  # Перенаправление на защищенную страницу
        else:
            flash('Неверное имя пользователя или пароль', 'danger')
    return render_template('login.html')  # Шаблон страницы входа

# Защищенная страница
@app.route('/protected')
@login_required  # Декоратор для защиты страницы


def protected():
    return f"<h1>Добро пожаловать, {current_user.username}!</h1><a href='/logout'>Выйти</a>"

# Страница выхода
@app.route('/logout')
@login_required
def logout():
    logout_user()  # Очистка данных пользователя из сессии
    flash('Вы вышли из системы', 'success')
    return redirect(url_for('home'))  # Перенаправление на главную страницу

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создание таблиц в базе данных при запуске приложения
    app.run(debug=True)
