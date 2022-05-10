from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=300)
    email = models.CharField(max_length=500)
    senha = models.CharField(max_length=30)