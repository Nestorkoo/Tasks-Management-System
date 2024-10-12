from django.urls import path, include

urlpatterns = [
    # Connect routers to tasks
    path('api/', include('TasksApp.urls')),
]