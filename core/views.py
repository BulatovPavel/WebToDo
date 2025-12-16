from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.decorators import login_required 
from .forms import TaskForm
from tasks.models import *
from datetime import date, timedelta
from django.contrib.auth import login
from .forms import TaskForm, RegisterForm 

def home(request):
    tasks_count = 0
    if request.user.is_authenticated:
        tasks_count = Task.objects.filter(user=request.user, is_completed=False).count()
        
    return render(request, 'core/index.html', {'tasks_count': tasks_count})

def contacts(request):
    return render(request, 'core/contacts.html')

@login_required
def task_list(request):
    return render(request, 'core/tasks.html')

@login_required
def calendar_view(request):
    return render(request, 'core/calendar.html')

@login_required
def profile(request):
    return render(request, 'core/profile.html')

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user 
            task.save()
            return redirect('tasks')
    else:
        form = TaskForm()

    return render(request, 'core/task_form.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'core/tasks.html', {'tasks': tasks})

@login_required
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_completed = not task.is_completed
    task.save()
    
    return redirect('tasks')

@login_required
def calendar_view(request):
    today = date.today() 
    start_of_week = today - timedelta(days=today.weekday())
    week_days = []
    
    for i in range(7):
        current_date = start_of_week + timedelta(days=i)
        day_tasks = Task.objects.filter(
            user=request.user, 
            due_date=current_date
        ).order_by('created_at')
        
        
        week_days.append({
            'date': current_date,
            'day_name': current_date.strftime('%A'), 
            'tasks': day_tasks,
            'is_today': (current_date == today) 
        })

    return render(request, 'core/calendar.html', {'week_days': week_days})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('home') 
    else:
        form = RegisterForm()
    
    return render(request, 'registration/register.html', {'form': form})