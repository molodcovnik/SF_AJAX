from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
    
    def get_last_messages():
        return Message.objects.order_by('-time').all()[:10]
    