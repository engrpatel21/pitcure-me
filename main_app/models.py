from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    pic = models.URLField(default='https://www.kindpng.com/picc/b/24/248253.png')
    
    def __str__(self):
        return f"Photo for user_id: {self.user_id} @{self.pic}"

    
class Photo(models.Model):
    url = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"Photo for user_id: {self.user_id} @{self.url}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    
   