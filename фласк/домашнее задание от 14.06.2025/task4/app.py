from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

# Модель записи блога
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    author = db.relationship('User', backref='posts')

# Создание таблиц в базе данных при первом запуске приложения
with app.app_context():
    db.create_all()

# Функции для работы с записями блога
def get_user_posts(user_id):
    return BlogPost.query.filter_by(author_id=user_id).all()

def add_blog_post(title, content, author_id):
    new_post = BlogPost(title=title, content=content, author_id=author_id)
    db.session.add(new_post)
    db.session.commit()

def update_blog_post(post_id, new_title=None, new_content=None):
    post = BlogPost.query.get(post_id)
    if post:
        if new_title:
            post.title = new_title
        if new_content:
            post.content = new_content
        db.session.commit()

def delete_blog_post(post_id):
    post = BlogPost.query.get(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
