from django.contrib import admin
from django.urls import path, include
from .views import index

app_name = 'awe'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('users/', include('users.urls', namespace='users')),
]
