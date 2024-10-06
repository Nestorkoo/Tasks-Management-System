from django.urls import path
from .views import TaskCreate, TaskList, TaskListSort

urlpatterns = [
    path('create/', TaskCreate.as_view(), name='create_task'),
    path('list/', TaskList.as_view(), name='list_task'),
    path('list/<str:status>/', TaskListSort.as_view(), name='sorted_list_task')

]
