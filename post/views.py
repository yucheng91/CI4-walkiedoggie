from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.
def walkingdog(request):
    return render(request, 'walkingdog.html')
    
def coverdog(request):
    post = Post.objects.all()
    return render(request, 'coverdog.html', {
        'post':post
    })
    
def create_coverdog(request):
    if request.method == 'POST':
        # process the from
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog_post = form.save(commit=False)
            new_blog_post.author = request.user
            new_blog_post.save()
            return redirect(reverse('coverdog'))
    else:
        form = PostForm()
        return render(request, 'create_coverdog.html', {
            'form': form
        })