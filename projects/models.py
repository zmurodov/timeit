from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = AutoSlugField('Slug', unique=True, always_update=False, populate_from='title')
    color = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    total_time = models.TimeField(blank=True, null=True)
    user = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Task(TimeStampedModel):
    STATUS_OPEN = 'open'
    STATUS_FINISHED = 'finished'
    STATUS_CHOICES = (
        (STATUS_OPEN, 'Open'),
        (STATUS_FINISHED, 'Finished'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_OPEN)
    is_tracking = models.BooleanField(default=False)

    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
