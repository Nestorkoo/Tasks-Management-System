from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Task
        fields = 'title', 'description', 'category', 'deadline'
    
    def create(self, validated_data):
        validated_data['category'] = validated_data['category'].lower()
        return super().create(validated_data)

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
class TaskEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = 'title', 'description', 'status', 'category', 'deadline'