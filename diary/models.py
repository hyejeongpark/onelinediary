from django.db import models

class Post(models.Model):
    drawing = models.ImageField()
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)