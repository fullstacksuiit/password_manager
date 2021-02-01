from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vault(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
