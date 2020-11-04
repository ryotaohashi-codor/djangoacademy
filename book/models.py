from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.TextField()

    def get_absolute_url(self):
        return f"/detail/{self.pk+1}"