from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    phone_number = models.CharField(
        max_length=20, unique=True, blank=True, null=True)
    telegram = models.CharField(
        max_length=50, unique=True, blank=True, null=True)
    adress = models.CharField(
        max_length=300, unique=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return f'USER: {self.user.username}'
