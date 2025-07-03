from django.urls import path
from parser import views

urlpatterns = [
    path('', views.parse_view),
]
