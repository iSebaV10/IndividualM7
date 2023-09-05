from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from datetime import date
from django.contrib.auth.views import LoginView
from django.urls import reverse

from .models import Task
from .forms import TaskForm

def index_view(request):
    return render(request, 'tasks/index.html')

def task_list(request):
    """
    Vista para mostrar la lista de tareas pendientes del usuario.
    """
    tasks = Task.objects.filter(assigned_to = request.user)
    #tasks = Task.objects.filter(user=request.user).order_by('due_date')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    """
    Vista para mostrar los detalles de una tarea.
    """
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})


def task_create(request, id):
    """
    Vista para crear una nueva tarea.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user_id = id
            task.save()
            return redirect('tasks_list')

    form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_edit(request, task_id):
    """
    Vista para editar una tarea existente.
    """
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, 'tasks/edit_form.html',{
            #"formEditTask": formEditTask
            'form': form, 'edit_mode': True, 'task': task
        })

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            #return redirect(reverse('task_detail', args=[task.id]))
            return redirect('task_detail', task_id=task_id)
    
   

@login_required
def task_delete(request, task_id):
    """
    Vista para eliminar una tarea.
    """
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@login_required
def task_mark_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.status = 'C'
    task.save()
    return redirect('tasks:task_detail', task_id=task.id)

def task_filter(request, status):
    if status == 'pending':
        tasks = Task.objects.filter(user=request.user, status='P').order_by('due_date')
    elif status == 'in_progress':
        tasks = Task.objects.filter(user=request.user, status='E').order_by('due_date')
    elif status == 'completed':
        tasks = Task.objects.filter(user=request.user, status='C').order_by('-due_date')
    else:
        return redirect('tasks:task_list')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_statistics(request):
    pending_count = Task.objects.filter(user=request.user, status='P').count()
    completed_count = Task.objects.filter(user=request.user, status='C').count()
    in_progress_count = Task.objects.filter(user=request.user, status='E').count()
    overdue_count = Task.objects.filter(user=request.user, status='P', due_date__lt=date.today()).count()

    return render(request, 'tasks/task_statistics.html', {
        'pending_count': pending_count,
        'completed_count': completed_count,
        'in_progress_count': in_progress_count,
        'overdue_count': overdue_count,
    })