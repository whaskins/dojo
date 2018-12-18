from django.db import models
from apps.login_app.models import User
# Create your models here.
class Message(models.Model):
    user_id = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=1000)
class Comment(models.Model):
    user_id = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    message_id = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    modified_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=1000)
