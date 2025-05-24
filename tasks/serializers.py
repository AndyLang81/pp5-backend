from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

# Serializer for Task model
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['owner', 'created_at']  # Set automatically