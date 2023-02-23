from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from todo.forms import TaskForm
from todo.models import Task, StatusChoice


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


def update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.details = form.cleaned_data['details']
            task.status = form.cleaned_data['status']
            task.completion_date = form.cleaned_data['completion_date']
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(initial={
            'description': task.description,
            'details': task.details,
            'status': task.status,
            'completion_date': task.completion_date,
        })
    return render(request, 'task_update.html', {'form': form, 'task': task})


def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    context = {
        'task': task,
    }
    return render(request, 'task_delete.html', context)
