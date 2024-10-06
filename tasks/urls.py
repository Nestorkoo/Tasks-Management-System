from django.urls import path
from .views import TaskCreate

urlpatterns = [
    path('create/', TaskCreate.as_view(), name='create_task'),

]
