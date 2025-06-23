from django.urls import path
from . import views

urlpatterns = [
    path('name/<str:username>/', views.greet_user, name='greet_user'),
]