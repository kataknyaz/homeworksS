from flask import Flask, render_template, redirect, url_for, flash
# Импортируем необходимые модули из Flask для создания приложения, работы с шаблонами,
# перенаправления и отображения сообщений.

from flask_sqlalchemy import SQLAlchemy
# Импортируем SQLAlchemy для работы с базой данных.

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# Импортируем необходимые классы и функции для управления пользователями и сессиями.

from werkzeug.security import generate_password_hash, check_password_hash
# Импортируем функции для хеширования паролей.

from forms import RegistrationForm, LoginForm, TaskForm
# Импортируем формы для регистрации, логина и управления задачами.

# Инициализация приложения Flask
app = Flask(__name__)  # Создаем экземпляр приложения Flask.
app.config['SECRET_KEY'] = 'your_secret_key'  # Устанавливаем секретный ключ для защиты сессий 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # Указываем URI для базы данных SQLite.
db = SQLAlchemy(app)  # Инициализируем SQLAlchemy с нашим приложением.
login_manager = LoginManager(app)  # Инициализируем менеджер логина с нашим приложением.
login_manager.login_view = 'login'  # Устанавливаем маршрут для страницы логина.

# Модель пользователя
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Идентификатор пользователя (первичный ключ).
    username = db.Column(db.String(150), unique=True, nullable=False)  # Имя пользователя 
    email = db.Column(db.String(150), unique=True, nullable=False)  # Email пользователя 
    password = db.Column(db.String(150), nullable=False)  # Пароль пользователя (обязательный, хранится в захешированном виде).
    tasks = db.relationship('Task', backref='owner', lazy=True)  # Связь с задачами

# Модель задачи
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Идентификатор задачи (первичный ключ).
    content = db.Column(db.String(300), nullable=False)  # Содержимое задачи 
    completed = db.Column(db.Boolean, default=False)  # Статус завершенности задачи 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Внешний ключ на пользователя

@login_manager.user_loader
def load_user(user_id):
    """Функция для загрузки пользователя по его идентификатору."""
    return User.query.get(int(user_id))  # Возвращаем пользователя по ID или None, если не найден.

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Маршрут для регистрации нового пользователя."""
    form = RegistrationForm()  #создаем экземпляр формы регистрации.
    if form.validate_on_submit():  # Проверяем, была ли форма отправлена и валидна ли она.
        hashed_password = generate_password_hash(form.password.data, method='sha256')  # Хешируем пароль.
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)  # Создаем нового пользователя.
        db.session.add(new_user)  # Добавляем нового пользователя в сессию базы данных.
        db.session.commit()  # Сохраняем изменения в базе данных.
        flash('Account created successfully!', 'success')  # Отображаем сообщение об успешной регистрации.
        return redirect(url_for('login'))  # Перенаправляем на страницу логина.
    return render_template('register.html', form=form)  # Отображаем форму регистрации.

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Маршрут для авторизации пользователя."""
    form = LoginForm()  # Создаем экземпляр формы логина.
    
    if form.validate_on_submit():  # Проверяем, была ли форма отправлена и валидна ли она.
        user = User.query.filter_by(email=form.email.data).first()  # Находим пользователя по email.
        
        # Проверяем, существует ли пользователь и корректен ли пароль.
        if user and check_password_hash(user.password, form.password.data):  
            login_user(user)  # Логиним пользователя, устанавливая сессию.
            return redirect(url_for('todo'))  # Перенаправляем на страницу задач.
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')  # Сообщение об ошибке логина.
    
    return render_template('login.html', form=form)  # Отображаем форму логина.


@app.route('/logout')
@login_required  # Требуется авторизация для выхода из системы.
def logout():
    """Маршрут для выхода из системы."""
    logout_user()  # Выход из системы.
    return redirect(url_for('login'))  # Перенаправляем на страницу логина.

@app.route('/todo', methods=['GET', 'POST'])
@login_required  # Требуется авторизация для доступа к задачам.
def todo():
    """Маршрут для отображения списка задач."""
    form = TaskForm()  # Создаем экземпляр формы для добавления новой задачи.
    if form.validate_on_submit():  # Проверяем, была ли форма отправлена и валидна ли она.
        new_task = Task(content=form.content.data, owner=current_user)  # Создаем новую задачу с текущим пользователем как владельцем.
        db.session.add(new_task)  # Добавляем новую задачу в сессию базы данных.
        db.session.commit()  # Сохраняем изменения в базе данных.
        flash('Task added successfully!', 'success')  # Сообщение об успешном добавлении задачи.
        return redirect(url_for('todo'))  # Перенаправляем на страницу задач.

    tasks = Task.query.filter_by(user_id=current_user.id).all()  # Получаем все задачи текущего пользователя из базы данных.
    return render_template('todo.html', form=form, tasks=tasks)  # Отображаем задачи текущего пользователя.

@app.route('/complete_task/<int:task_id>')
@login_required  # Требуется авторизация для завершения задачи.
def complete_task(task_id):
    """Маршрут для завершения задачи."""
    task = Task.query.get_or_404(task_id)  # Находим задачу по ID или возвращаем ошибку 404, если не найдена.
    task.completed = True  # Устанавливаем статус завершенности задачи в True.
    db.session.commit()  # Сохраняем изменения в базе данных.
    return redirect(url_for('todo'))  # Перенаправляем на страницу задач.

@app.route('/delete_task/<int:task_id>')
@login_required  # Требуется авторизация для удаления задачи.
def delete_task(task_id):
    """Маршрут для удаления задачи."""
    task = Task.query.get_or_404(task_id)  # Находим задачу по ID или возвращаем ошибку 404, если не найдена.
    db.session.delete(task)  # Удаляем задачу из сессии базы данных.
    db.session.commit()  # Сохраняем изменения в базе данных.
    return redirect(url_for('todo'))  # Перенаправляем на страницу задач.

@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
@login_required  # Требуется авторизация для редактирования задачи.
def edit_task(task_id):
    """Маршрут для редактирования задачи."""
    task = Task.query.get_or_404(task_id)  # Находим задачу по ID или возвращаем ошибку 404, если не найдена.
    form = TaskForm(obj=task)  # Создаем форму редактирования с данными текущей задачи.

    if form.validate_on_submit():  # Проверяем, была ли форма отправлена и валидна ли она.
        task.content = form.content.data  # Обновляем содержимое задачи новым значением из формы.
        db.session.commit()  # Сохраняем изменения в базе данных.
        return redirect(url_for('todo'))  # Перенаправляем на страницу задач.

    return render_template('edit_task.html', form=form)  # Отображаем форму редактирования.

if __name__ == '__main__':
    db.create_all()  # Создание всех таблиц в базе данных при первом запуске приложения.
    app.run(debug=True)  
