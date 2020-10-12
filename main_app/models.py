from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    pic = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Photo for cat_id: {self.cat_id} @{self.url}"

    
