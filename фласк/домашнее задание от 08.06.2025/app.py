from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from models import db, Feedback


# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Настройки приложения
app.config['SECRET_KEY'] = 'your_secret_key'  # Секретный ключ для защиты форм
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'  # URI для подключения к базе данных SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Отключаем отслеживание изменений объектов


db.init_app(app)# Инициализируем базу данных с приложением

# Определяем форму обратной связи с помощью Flask-WTF
class FeedbackForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])  # Поле для имени с обязательной валидацией
    email = StringField('Email', validators=[DataRequired(), Email()])  # Поле для email с валидацией на корректность формата
    message = TextAreaField('Сообщение', validators=[DataRequired()])  # Поле для сообщения с обязательной валидацией
    submit = SubmitField('Отправить')  # Кнопка отправки формы

# Маршрут для формы обратной связи
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()  # Создаем экземпляр формы
    if form.validate_on_submit():  # Проверяем, была ли форма отправлена и валидна ли она
        # Создаем новый объект Feedback с данными из формы
        feedback = Feedback(
            name=form.name.data,
            email=form.email.data,
            message=form.message.data
        )
        db.session.add(feedback)  # Добавляем объект в сессию базы данных
        db.session.commit()  # Сохраняем изменения в базе данных
        return redirect(url_for('feedback_list'))  # Перенаправляем на страницу со списком отзывов
    
    return render_template('feedback.html', form=form)  # Отображаем форму

# Маршрут для отображения списка отзывов
@app.route('/feedback_list')
def feedback_list():
    feedbacks = Feedback.query.all()  # Получаем все отзывы из базы данных
    return render_template('feedback_list.html', feedbacks=feedbacks)  # Отображаем список отзывов

# Запуск приложения
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создаем таблицы в базе данных при первом запуске
    app.run(debug=True)  
