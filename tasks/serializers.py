from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = 'title', 'description', 'category', 'deadline'

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
class TaskEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = 'title', 'description', 'status', 'category', 'deadline'