from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


def generate_uuid():
    return uuid.uuid4().hex[:40]

class User(AbstractUser):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=40)
    avatar = models.ImageField(upload_to='profile/', default='profile/avatar.png', null=True, blank=True)
    background_image = models.ImageField(upload_to='background/', null=True, blank=True)

    def __str__(self):
        return self.username;
