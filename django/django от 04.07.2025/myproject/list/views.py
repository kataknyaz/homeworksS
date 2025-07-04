# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category
from .forms import TaskForm, CategoryForm

def task_list(request):
    tasks = Task.objects.all()
    
    # Фильтрация по категории
    category_id = request.GET.get('category')
    if category_id:
        tasks = tasks.filter(category_id=category_id)

    # Сортировка по дате создания и приоритету
    sort_by = request.GET.get('sort_by', 'created_at')
    tasks = tasks.order_by(sort_by)

    categories = Category.objects.all()
    
    return render(request, 'task_list.html', {'tasks': tasks, 'categories': categories})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'task_form.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')
