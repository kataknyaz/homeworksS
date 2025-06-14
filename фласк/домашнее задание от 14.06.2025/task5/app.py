from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/update_profile', methods=['POST'])
def update_profile():
    # Логика обновления профиля...
    
    # После успешного обновления
    flash('Профиль обновлен!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
