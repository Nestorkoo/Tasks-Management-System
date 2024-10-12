from celery import shared_task
from .models import Task, Notification
from datetime import timedelta
from django.utils import timezone

@shared_task
def add_status_overdue():
    now = timezone.now()

    one_minute = timedelta(minutes=1)
    tasks = Task.objects.filter(deadline__gte=now - one_minute, deadline__lte=now + one_minute)

    if tasks.exists():
        for task in tasks:
            print(f'Task is overdue: {task.title}')
    else:
        print('None')