from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # сразу авторизует
            return redirect('post_list')  # после регистрации на список постов
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def post_list(request):
    posts = Post.objects.all().order_by('-created_date', '-created_date')

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.views += 1
    post.save(update_fields=['views'])

    return render(request, 'blog/post_detail.html',{'post': post})