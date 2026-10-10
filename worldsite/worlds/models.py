from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class World(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)
