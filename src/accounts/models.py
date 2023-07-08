from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField(max_length=1024, null=True)
    photo = models.ImageField(upload_to='images/%Y/%m/%d/', null=True)

    def __str__(self):
        return f'{self.user}'
    
    def get_absolute_url(self):
        return reverse('accounts:profile', args=[str(self.id)])