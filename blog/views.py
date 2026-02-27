from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_date', '-created_date')

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.views += 1
    post.save(update_fields=['views'])

    return render(request, 'blog/post_detail.html',{'post': post})