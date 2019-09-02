from django.db import models
from accounts.models import MyUser

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title
        
class AdminPost(models.Model):
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title