from django.urls import path

from . import views


app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_task, name='create_task'),
    path('profile/', views.profile, name='profile'),
]
