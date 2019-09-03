from django import forms
from .models import Post, AdminPost
from pyuploadcare.dj.forms import ImageField

class PostForm(forms.ModelForm):
    cover = ImageField(label='Photo')
    class Meta:
        model = Post
        fields = ('title', 'content','cover')
        
class AdminPostForm(forms.ModelForm):
    cover = ImageField(label='Photo')
    class Meta:
        model = AdminPost
        fields = ('title', 'content','cover')