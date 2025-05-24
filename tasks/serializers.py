from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


# Serializer for Task model
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['owner']


# Serializer for User model (optional: for listing users later)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
