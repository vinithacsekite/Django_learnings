from . import views
from django.urls import path

urlpatterns = [
    path('task-list/', views.task_list_view, name='task_list'),
    path('create-task/', views.create_task_view, name='create-task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete-task'),
     path('update/<int:task_id>/', views.update_task, name='update-task'),
    
]