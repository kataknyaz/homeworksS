from django.shortcuts import render, get_object_or_404

posts = [
    {
        'id': 1,
        'title': 'Моя первая статья',
        'text': 'Это текст первой статьи...',
        'date': '19.06.2024',

    },
    {
        'id': 2,
        'title': 'Вторая статья про Django',
        'text': 'Сегодня я изучаю шаблон в Django...',
        'date': '20.06.2024'
    }
]

def index(request):
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(posts, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
