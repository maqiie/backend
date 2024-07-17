from django.urls import path
from .views import task_list_create, task_reschedule, task_delete
from .views import complete_task  # Make sure to import complete_task here

urlpatterns = [
    path('tasks/', task_list_create, name='task-list-create'),
    path('tasks/<int:pk>/reschedule/', task_reschedule, name='task-reschedule'),
    path('tasks/<int:pk>/delete/', task_delete, name='task-delete'),
    path('tasks/<int:pk>/complete/', complete_task, name='complete_task'),

]
