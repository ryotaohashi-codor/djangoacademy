from django.db import models

# Create your models here.

CHOICES = ((1,'Morning'), (2,'Afternoon'))
class Book(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True, null=True)
    content = models.TextField(default='some content')
    author = models.CharField(max_length=10)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = 'some title'
        super(Book, self).save(*args, **kwargs)
    
    def age(self):
        return 'a'

