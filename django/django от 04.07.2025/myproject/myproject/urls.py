# urls.py
from django.urls import path
from .views import task_list, task_create, task_edit, task_delete

urlpatterns = [
    path('', task_list, name='task_list'),
    path('task/create/', task_create, name='task_create'),
    path('task/edit/<int:pk>/', task_edit, name='task_edit'),
    path('task/delete/<int:pk>/', task_delete, name='task_delete'),
]

