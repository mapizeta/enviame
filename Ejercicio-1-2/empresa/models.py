from django.db import models

# Create your models here.
class Empresa(models.Model):
    empresa_name = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    