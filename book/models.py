from django.db import models

# Create your models here.

class File(models.Model):
    title = models.TextField()
    file = models.FileField()
    