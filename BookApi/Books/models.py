from django.db import models

# Create your models here.
# books/models.py

from django.db import models
from django.contrib.auth.models import User

class BookRecommendation(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='book_likes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    recommendation = models.ForeignKey(BookRecommendation, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    