from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Главная страница
    path('post/<int:post_id>/', views.post_detail, name='post_detail'), #Страница статьи
]