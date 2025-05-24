from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer

# View that lets logged-in users list and create their own tasks
class TaskListCreate(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Return only tasks belonging to the logged-in user
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    # Save the task with the current user as the owner
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# View to retrieve, update, or delete a single task by ID
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Again, limit access to only the user's own tasks
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
