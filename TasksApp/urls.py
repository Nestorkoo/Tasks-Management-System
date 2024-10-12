from django.urls import path
from .views import TaskCreate, TaskList, TaskListSort, EditTask, TaskDelete, StatisticTasks, StatisticByCategory

urlpatterns = [
    path('create/', TaskCreate.as_view(), name='create_task'),
    path('list/', TaskList.as_view(), name='list_task'),
    path('list/<str:status>/', TaskListSort.as_view(), name='sorted_list_task'),
    path('task/<int:pk>/update/', EditTask.as_view(), name='edit_Task'),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name='task-delete'),
    path('task/stat_count/', StatisticTasks.as_view(), name='task_statistic_count'),
    path('task/stat_cat/<str:category>/', StatisticByCategory.as_view(), name='task_stat_category'),
    

]
