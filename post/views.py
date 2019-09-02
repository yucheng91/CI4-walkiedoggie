from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
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
        pass
    else:
        form = PostForm()
        return render(request, 'create_coverdog.html', {
            'form': form
        })
        
def edit_coverdog(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            new_blog_post = form.save(commit=False)
            new_blog_post.author = request.user
            new_blog_post.save()
            return redirect('coverdog')
    else:
        form = PostForm(instance=post)
        return render(request, 'create_coverdog.html',{
            'form':form
        })
        