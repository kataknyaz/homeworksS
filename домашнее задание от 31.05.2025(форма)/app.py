from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Замените на свой секретный ключ

class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[
        DataRequired(),
        Length(min=3, max=20),
        Regexp(r'^[А-яЁёs]+$', message='Необходимо ввести имя и фамилию на русском языке')
    ])

    email = StringField('Email', validators=[
        DataRequired(),
        Email(message='некорректный Email')
    ])

    password = PasswordField('Пароль', validators=[
        DataRequired(),
        Length(min=8, message='Пароль должен быть не менее 8 символов')
    ])

    confirm_password = PasswordField('Повторите пароль', validators=[
        DataRequired(),
        EqualTo('password', message='пароли должны совпадать')        
    ])

    submit = SubmitField('Зарегистрироваться')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Здесь можно добавить логику для сохранения пользователя в базу данных
        return redirect(url_for('index'))  # Перенаправление на главную страницу после успешной регистрации

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)



