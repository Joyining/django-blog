from django.db import models
from datetime import datetime

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, default='Untitled post')
    body = models.CharField(max_length=100000, default='')
    author = models.CharField(max_length=100, default='Unknown author')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    thumbnail = models.ImageField(upload_to='uploads', default='')

    GENERAL = 0
    DEV_OPS = 1
    WEB3 = 2
    LIFE = 3
    CATEGORY_CHOICES = [
        (GENERAL, 'General'),
        (DEV_OPS, 'DevOps'),
        (WEB3, 'Web3'),
        (LIFE, 'Life'),
    ]
    category = models.IntegerField(
        choices=CATEGORY_CHOICES,
        default=GENERAL,
    )

    def __str__(self):
        return self.title
