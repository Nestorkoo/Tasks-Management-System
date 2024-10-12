from __future__ import absolute_import, unicode_literals
import os 
from celery import Celery 
from celery.schedules import crontab

os. environ.setdefault('DJANGO_SETTINGS_MODULE', 'SCT.settings')

app = Celery('SCT')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    "add_status_overdue-every-2-minutes": {
        "task": "TasksApp.tasks.add_status_overdue",
        "schedule": crontab(minute="*/2"),  # Кожні 2 хвилини
    },
}


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request {self.request!r}")