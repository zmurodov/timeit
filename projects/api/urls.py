from django.urls import path
from . import views as v

app_name = 'projects-api'

urlpatterns = [
    path('projects/', v.ProjectListCreateAPIView.as_view(), name='api-project-list'),
    path('projects/<int:pk>/', v.ProjectDetailsApiView.as_view(), name='api-project-details'),
    path('projects/<int:pk>/tasks/', v.TaskListAPIView.as_view(), name='api-task-list'),
    path('projects/<int:pk>/task/', v.TaskCreateAPIView.as_view(), name='api-task-create'),
    path('tasks/<int:pk>/', v.TaskDetailApiView.as_view(), name='api-task-detail'),
    path('tasks/<int:pk>/stop/', v.TaskTimeStopAPIView.as_view(), name='api-task-stop'),
    # path('tasks/<int:pk>/resume/', v.TaskTimeResumeAPIView.as_view(), name='api-task-resume'),
]
