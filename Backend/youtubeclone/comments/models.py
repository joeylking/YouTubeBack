from django.db import models
from django.db.models.fields import related

# Create your models here.
class Comment(models.Model):
    video = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return self.author