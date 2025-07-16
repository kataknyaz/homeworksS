from django.urls import path
from articles.views import article_list, register, login_view, logout_view, create_article, article_detail

urlpatterns = [
    path('', article_list, name='article_list'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('article/new/', create_article, name='create_article'),
    path('article/<int:id>/', article_detail, name='article_detail'),
   ]
   