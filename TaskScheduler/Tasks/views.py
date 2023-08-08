from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def task_list_view(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html',{ 'tasks':tasks})


def create_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')    
    else:
        form = TaskForm()
    
    return render(request, 'create_task.html', {'form': form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
    return redirect('task_list')  



def update_task(request, task_id):
    if request.method == 'POST':
        completed = request.POST.get('completed') == 'on' 
        task = Task.objects.get(id=task_id)
        task.completed = completed
        task.save()

        return redirect('task_list') 