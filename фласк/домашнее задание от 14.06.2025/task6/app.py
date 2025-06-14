from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Главная страница с приветствием
    return render_template('home.html')

@app.route('/user/<username>')
def profile(username):
    # Страница профиля пользователя
    return render_template('profile.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
