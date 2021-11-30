from django.db import models
from django.db.models.fields import related

# Create your models here.
class Comment(models.Model):
    video_id = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name="replies", blank=True, null=True)

    def __str__(self):
        return self.author