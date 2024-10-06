from django.urls import path, include

urlpatterns = [
    path('api/', include('tasks.urls')),  # Connect routers to tasks
]