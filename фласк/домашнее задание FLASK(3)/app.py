from flask import Flask, render_template

app = Flask(__name__)


users = ["Алексей", "Мария", "Иван"]

@app.route('/')
def index():
    is_logged_in = True  
    user_role = "User"  
    return render_template('index.html', is_logged_in=is_logged_in, user_role=user_role, users=users)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)



