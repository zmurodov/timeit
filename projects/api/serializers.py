from rest_framework import serializers

from projects.models import Project, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['project', 'is_tracking', ]


class ProjectListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = ('pk', 'title', 'slug', 'color', 'description', 'total_time', 'user',)


class ProjectDetailSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, required=False, read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = ('pk', 'title', 'slug', 'color', 'description', 'total_time', 'user', 'tasks')
