from django.contrib.auth.models import User
from django.db import models
import django

class Post(models.Model):
    """
    Modelo del Post (menu)
    """
    title = models.CharField(max_length=200, null=False)
    paragraph = models.TextField(null=False)
    date = models.DateTimeField(default=django.utils.timezone.now, null=False)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__ (self):
        return str(self.id) + ' ' + self.title

class Usuario(models.Model):
    """
    Modelo del usuario
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, default=1)
    avatar = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return str(self.user)
