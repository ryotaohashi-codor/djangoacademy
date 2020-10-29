from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.TextField()
    content = models.TextField()