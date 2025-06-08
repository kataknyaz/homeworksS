from flask_sqlalchemy import SQLAlchemy

# Создаем экземпляр SQLAlchemy
db = SQLAlchemy()

# Определяем модель Feedback
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Идентификатор отзыва
    name = db.Column(db.String(100), nullable=False)  # Имя пользователя
    email = db.Column(db.String(120), nullable=False)  # Email пользователя
    message = db.Column(db.Text, nullable=False)  # Сообщение отзыва

    def __repr__(self):
        return f'<Feedback {self.name}, {self.email}>'  

