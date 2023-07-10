from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
    
    def get_last_messages(self):
        return Message.objects.order_by('-time').all()[:10]

class Chat(models.Model):
    chat_name = models.TextField(max_length=255, unique=True)
    messages = models.ManyToManyField(Message, blank=True)
    members = models.ManyToManyField(User, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.chat_name}'
    
    def get_absolute_url(self):
        return reverse('chat:create_chat', args=[str(self.chat_name)])

