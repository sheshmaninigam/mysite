from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, default='1')
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_picture')
    location = models.CharField(max_length=100)
    user_type = models.CharField(max_length=200,default="user")

    def __str__(self):
        return self.user.username
