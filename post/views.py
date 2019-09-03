from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from .models import Post, AdminPost
from .forms import PostForm, AdminPostForm

# Post views setting for Walking Dog page (Only for superuser to create/modify/delete)

def walkingdog(request):
    post = AdminPost.objects.all()
    return render(request, 'walkingdog.html', {
        'post': post
    })
    
def create_walkingdog(request):
    if request.method == 'POST':
        form = AdminPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog_post = form.save(commit=False)
            new_blog_post.author = request.user
            new_blog_post.save()
            return redirect(reverse('walkingdog'))
        pass
    else:
        form = AdminPostForm()
        return render(request, 'create_walkingdog.html', {
            'form': form
        })
        
def edit_walkingdog(request, id):
    post = get_object_or_404(AdminPost, pk=id)
    if request.method == 'POST':
        form = AdminPostForm(request.POST, instance=post)
        if form.is_valid():
            new_blog_post = form.save(commit=False)
            new_blog_post.author = request.user
            new_blog_post.save()
            return redirect(reverse('walkingdog'))
    else:
        form = AdminPostForm(instance=post)
        return render(request, 'create_walkingdog.html',{
            'form':form
        })
        
def delete_walkingdog(request, id):
    post = get_object_or_404(AdminPost, id=id)
    if request.method =='POST':
        post.delete()
        return redirect(reverse('walkingdog'))
    else:
        return render (request,"delete_walkingdog.html",{
            'post': post
        })
        
# Post views setting for Cover Dog page (Registered user can upload only. Superuser aka Admin to modify/delete)
    
def coverdog(request):
    post = Post.objects.all()
    return render(request, 'coverdog.html', {
        'post': post
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
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_blog_post = form.save(commit=False)
            new_blog_post.author = request.user
            new_blog_post.save()
            return redirect(reverse('coverdog'))
    else:
        form = PostForm(instance=post)
        return render(request, 'create_coverdog.html',{
            'form':form
        })
        
def delete_coverdog(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method =='POST':
        post.delete()
        return redirect(reverse('coverdog'))
    else:
        return render (request,"delete_coverdog.html",{
            'post': post
        })
        
def vote_coverdog(request, id):
    post = get_object_or_404(Post, id=id)
    post.score += 1
    post.save()
    return redirect(reverse('coverdog'))