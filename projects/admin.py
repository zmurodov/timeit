from django.contrib import admin

from .models import Project, Task


class TaskInline(admin.StackedInline):
    model = Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (TaskInline,)


admin.site.register(Task)
