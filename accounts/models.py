from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Device(models.Model):
    user = models.ForeignKey(User, related_name='devices', on_delete=models.CASCADE)
    hardware_key = models.CharField(max_length=120)

    def __str__(self):
        return self.user.username
