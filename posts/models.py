from django.db import models
from datetime import datetime

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, default='Untitled post')
    body = models.CharField(max_length=100000, default='')
    author = models.CharField(max_length=100, default='Unknown author')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    thumbnail = models.ImageField(upload_to='uploads', default='')

    def __str__(self):
        return self.title
