from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

# Создаем экземпляр Flask
app = Flask(__name__)
Bootstrap(app)

# Главная страница
@app.route('/')
def index():
    # Отправляем на главную страницу, используя шаблон index.html
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])   # Страница с формой для ввода данных
def form():
    # Если запрос метода POST (если форма была отправлена)
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form['name']
        email = request.form['email']        
        return redirect(url_for('thank_you', name=name))   # Перенаправляем пользователя на страницу благодарности с именем
    
    return render_template('form.html') # Если это GET-запрос, просто отображаем форму


@app.route('/thank_you/<name>')# Страница благодарности после отправки формы
def thank_you(name):
    # Отправляем сообщение с благодарностью
    return f"Спасибо, {name}, за вашу регистрацию!"

if __name__ == '__main__':
    app.run(debug=True)  
