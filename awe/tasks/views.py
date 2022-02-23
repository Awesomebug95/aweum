from django.shortcuts import render

from tasks.forms import TaskForm


def index(request):
    return render(request, 'tasks/index.html')


def profile(request):
    return render(request, 'tasks/profile.html')


def create_task(request):
    form = TaskForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'tasks/create_task.html', {'form': form})
    form.instance.author = request.user
    form.save()
    return render(request, 'tasks/create_task.html', {'form': form})
