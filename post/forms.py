from django import forms
from .models import Post, AdminPost

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content','cover')
        
class AdminPostForm(forms.ModelForm):
    class Meta:
        model = AdminPost
        fields = ('title', 'content','cover')