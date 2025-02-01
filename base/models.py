from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Posts(models.Model):
    Title = models.CharField(max_length=100)
    description= models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null= True, blank=True)
    image = models.ImageField(null= True, blank= True)

    def __str__(self):
        return f'{self.user.username} Profile'
    