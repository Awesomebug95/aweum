from django.shortcuts import render


def index(request):
    return render(request, 'tasks/index.html')


def profile(request):
    return render(request, 'tasks/profile.html')


def create_task(request):
    return render(request, 'tasks/create_task.html')