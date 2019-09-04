from django import forms
from .models import Post, AdminPost
from pyuploadcare.dj.forms import ImageField

class PostForm(forms.ModelForm):
    cover = ImageField(label='Photo')
    class Meta:
        model = Post
        labels = {
            "title":"Name",
            "age" : "Estimated Age",
            "sex" : "Gender",
            "content":"Intro"
        }
        fields = ('title','age','sex','content','cover')
        
class AdminPostForm(forms.ModelForm):
    cover = ImageField(label='Photo')
    class Meta:
        model = AdminPost
        labels = {
            "title":"Name",
            "age" : "Estimated Age",
            "sex" : "Gender",
            "content":"Intro"
        }
        fields = ('title','age','sex','content','cover')