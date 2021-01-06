import datetime
from django.utils import timezone
from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     get_object_or_404)
from projects.api.serializers import ProjectListSerializer, ProjectDetailSerializer, TaskSerializer
from projects.api.permissions import IsProjectOwner, IsTaskOwner
from projects.models import Project, Task


class ProjectListCreateAPIView(ListCreateAPIView):
    serializer_class = ProjectListSerializer
    permission_classes = [IsAuthenticated, IsProjectOwner]

    def get_queryset(self):
        user = self.request.user
        qs = Project.objects.filter(user=user).order_by('-created_at')
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectDetailsApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated, IsProjectOwner]

    def get_queryset(self):
        user = self.request.user
        qs = Project.objects.filter(user=user)
        return qs


class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsTaskOwner]

    def get_queryset(self):
        project_pk = self.kwargs.get("pk")
        user = self.request.user
        # project = get_object_or_404(Project, pk=project_pk)
        project = get_object_or_404(Project, pk=project_pk, user=user)
        return Task.objects.filter(project=project).order_by('-created_at')


class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsTaskOwner]

    def perform_create(self, serializer):
        project_pk = self.kwargs.get("pk")
        project = get_object_or_404(Project, pk=project_pk, user=self.request.user)

        serializer.save(project=project)


class TaskDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated, IsTaskOwner]


class TaskTimeStopAPIView(views.APIView):
    permission_classes = [IsAuthenticated, IsTaskOwner]

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        user = request.user
        task = get_object_or_404(Task, pk=pk, project__user=user)

        is_tracking = task.is_tracking
        if not is_tracking:
            now = timezone.now().time()
            time = task.time
            print(time)
            print(now)
            # print((time - now).timestamp())

        return Response(status=status.HTTP_200_OK)
