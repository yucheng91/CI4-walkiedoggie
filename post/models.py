from django.db import models
from accounts.models import MyUser
from pyuploadcare.dj.models import ImageField 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    age = models.CharField(max_length=50, default="")
    sex = models.CharField(max_length=30, default="")
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    cover = ImageField(blank=True)
    score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
        
class AdminPost(models.Model):
    title = models.CharField(max_length=255, blank=False)
    age = models.CharField(max_length=50, default="")
    sex = models.CharField(max_length=30, default="")
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    cover = ImageField(blank=True)

    def __str__(self):
        return self.title