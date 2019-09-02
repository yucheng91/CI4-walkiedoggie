from django.contrib import admin
from .models import Post, AdminPost


# Register your models here.
admin.site.register(Post)
admin.site.register(AdminPost)