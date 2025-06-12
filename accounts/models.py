from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='profile_path')
    
    def __str__(self):
        return self.bio