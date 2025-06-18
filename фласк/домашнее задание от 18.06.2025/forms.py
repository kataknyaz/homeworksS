from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    """Форма регистрации нового пользователя."""
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=150)])  # Поле имени пользователя с проверкой на обязательность и длину
    email = StringField('Email', validators=[DataRequired(), Email()])  # Поле email с проверкой на обязательность и формат email
    password = PasswordField('Password', validators=[DataRequired()])  # Поле пароля с проверкой на обязательность
    submit = SubmitField('Sign Up')  # Кнопка отправки формы

class LoginForm(FlaskForm):
    """Форма логина пользователя."""
    email = StringField('Email', validators=[DataRequired(), Email()])  # Поле email с проверкой на обязательность и формат email
    password = PasswordField('Password', validators=[DataRequired()])  # Поле пароля с проверкой на обязательность
    submit = SubmitField('Login')  # Кнопка отправки формы

class TaskForm(FlaskForm):
    """Форма для добавления или редактирования задачи."""
    content = TextAreaField('Task', validators=[DataRequired()])  # Поле для ввода текста задачи с проверкой на обязательность
    submit = SubmitField('Add Task')  # Кнопка отправки формы для добавления задачи
