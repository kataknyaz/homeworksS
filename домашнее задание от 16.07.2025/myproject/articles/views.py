from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Article


def article_list(request):
    articles = Article.objects.all() # вСЕ СТАТЬИ ИЗ БАЗЫ ДАННЫХ
    return render(request, 'articles/article_list.html', {'articles': articles}) # отправка статьи в шаблон
def register(request):
    if request.method == 'POST': # если метод пост
        form = UserCreationForm(request.POST) # создаем форму с данными из запроса
        if form.is_valid():   # если форма валидна 
            user = form.save() # созраняем нового пользователя
            login(request, user) # входим в систему под новым пользователем
            return redirect('article_list') # перенапрявляем на страницу со списком статей
    else:
        form = UserCreationForm() # иначе пустая форма
    return render(request, 'articles/register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username'] # получаем имя пользователя из запроса
        password = request.POST['password'] # получаем пароль пользователя из запроса
        user = authenticate(request, username=username, password=password) # аутентификация
        if user is not None: # если пользователь найден
            login(request, user) # входим в систему
            return redirect('article_list')
        else:
            return render(request, 'articles/login.html', {'error': 'Invalid credentials'}) # если ошибка, то выводим сообщение об ошибке 
    return render(request, 'articles/login.html')
def logout_view(request):
    logout(request)
    return redirect('article_list')
def create_article(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        article = Article(title=title, content=content, author=request.user)
        article.save()
        return redirect('article_list')
    return render(request, 'articles/create_article.html')
def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'articles/article_detail.html', {'article': article})
   