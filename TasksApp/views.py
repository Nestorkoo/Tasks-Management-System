from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import TaskSerializer, TaskListSerializer, TaskEditSerializer
from rest_framework import status as st
from .models import Task


class TaskCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=st.HTTP_201_CREATED)
        return Response(serializer.errors, status=st.HTTP_400_BAD_REQUEST)

class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer

    def get(self, request, *args, **kwargs):
        tasks = self.get_queryset()
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data, st.HTTP_200_OK)
        
class TaskListSort(generics.ListAPIView):
    serializer_class = TaskListSerializer
    queryset = Task.objects.all()

    def get(self, request, *args, **kwargs):
        status = self.kwargs.get('status')
        queryset = self.queryset

        if status:
            queryset = queryset.filter(status=status)
            
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=st.HTTP_200_OK)

class EditTask(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskEditSerializer

    def put(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = self.get_serializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save()  # Зберігаємо оновлені дані
            return Response(serializer.data, status=st.HTTP_200_OK)  # Повертаємо оновлені дані

        return Response(serializer.errors, status=st.HTTP_400_BAD_REQUEST)

class TaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer

    def delete(self, request, *args, **kwargs):
        task = self.get_object()
        task.delete()
        return Response('Succesful deleted!',status=st.HTTP_200_OK)

class StatisticTasks(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        task_count = Task.objects.count()
        return Response(f"Total task: {task_count}", status=st.HTTP_201_CREATED)

class StatisticByCategory(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer

    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category')
        queryset = self.queryset
        
        if category:
            queryset = queryset.filter(category=category)
        
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "message": "Tasks with a category:",
            'tasks': serializer.data
        }, status=st.HTTP_200_OK)
