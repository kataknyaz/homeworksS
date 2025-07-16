from django.db import models  
from django.contrib.auth.models import User  

class Article(models.Model):  # Определяем модель Article
    title = models.CharField(max_length=200)  # Заголовок статьи
    content = models.TextField()  # Содержимое статьи
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор статьи 
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания статьи
    updated_at = models.DateTimeField(auto_now=True)  # Дата и время последнего обновления статьи
    def __str__(self):
        return self.title  