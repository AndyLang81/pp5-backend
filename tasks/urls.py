from django.urls import path
from .views import TaskListCreate, TaskDetailView

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]
