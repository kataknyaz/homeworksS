from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

def parse_view(request):
    # По умолчанию показываем пустую форму
    context = {}
    
    # Если форма отправлена (POST-запрос)
    if request.method == 'POST':
        url = request.POST.get('url', '')  # Получаем URL из формы
        
        try:
            # Загружаем страницу с пользовательским заголовком
            headers = {'User-Agent': 'Mozilla/5.0'}
            page = requests.get(url, headers=headers)
            page.raise_for_status()  # Проверяем на ошибки
            
            # Парсим HTML с помощью BeautifulSoup
            soup = BeautifulSoup(page.text, 'html.parser')
            
            # Собираем основные данные
            context = {
                'url': url,
                'title': soup.title.string if soup.title else 'Без заголовка',
                'text': ' '.join(p.get_text() for p in soup.find_all('p')),  # Весь текст из параграфов
                'success': True  # Флаг успешного парсинга
            }
            
        except Exception as e:
            context['error'] = f'Ошибка: {str(e)}'  # Сообщение об ошибке
    
    return render(request, 'parser.html', context)
