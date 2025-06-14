from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Замените на свой секретный ключ
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Используем SQLite для простоты
db = SQLAlchemy(app)

# Модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

# Создание таблиц в базе данных при запуске приложения
with app.app_context():
    db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():  # Проверка валидности формы
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)  # Добавляем пользователя в сессию
        db.session.commit()  # Сохраняем изменения в базе данных
        flash('Вы успешно зарегистрированы!', 'success')  # Сообщение об успешной регистрации
        return redirect(url_for('home'))  # Перенаправление на главную страницу

    return render_template('register.html', form=form)  # Отображение формы регистрации

@app.route('/')
def home():
    return "<h1>Главная страница</h1>"

if __name__ == '__main__':
    app.run(debug=True)
