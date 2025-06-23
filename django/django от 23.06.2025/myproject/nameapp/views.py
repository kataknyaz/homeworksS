from django.http import HttpResponse

def greet_user(request, username):
    return HttpResponse(f'Привет, {username}')
