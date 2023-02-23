from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from todo.forms import TaskForm
from todo.models import Task


def index_view(request: WSGIRequest):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context=context)


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'task_create.html', {'form': form})
    form = TaskForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'task_create.html', context={
            'form': form
        })
    else:
        task = Task.objects.create(**form.cleaned_data)
        return redirect('task_detail', pk=task.pk)


def detailed_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', context={'task': task})
