from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Task


def index_view(request: WSGIRequest):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context=context)


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'task_create.html', {'task': Task()})
    task_data = {
        'description': request.POST.get('description'),
        'details': request.POST.get('details'),
        'status': request.POST.get('status'),
        'completion_date': request.POST.get('completion_date')
    }
    task = Task.objects.create(**task_data)
    return redirect('task_detail', pk=task.pk)


def detailed_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', context={'task': task})
