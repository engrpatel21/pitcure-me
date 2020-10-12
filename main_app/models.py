from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    pic = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Photo for user_id: {self.user_id} @{self.pic}"

    
class Photo(models.Model):
    url = models
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Photo for user_id: {self.user_id} @{self.url}"