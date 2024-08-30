from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from .forms import PostForm
from .models import Post


def root(request):
    return render(request, template_name='blog/index.html')

def index(request):
    return render(request, template_name='blog/index.html')

def about(request):
    context = {
        "name": "Dmitri",
        "lastname": "Gorin",
        "email": "d.gorin@yandex.ru",
        "title": "About site"
    }
    return render(request, template_name='blog/about.html', context=context)


@login_required
def add_post(request):
    if request.method == "GET":
        form = PostForm(author=request.user)
        context = {
            'form': form,
            'title': 'Post adding'
        }
        return render(request, template_name='blog/add_post.html', context=context)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, author=request.user)
        if form.is_valid():
            form.save()

        return index(request)


def post_list(request):
    posts = Post.objects.all()
    context = {
        'title': 'Posts',
        'posts': posts
    }
    return render(request, template_name='blog/posts.html', context=context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'title': 'Post information',
        'post': post
    }
    return render(request, template_name='blog/post_detail.html', context=context)


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return post_list(request)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'title': 'Edit post'
    }
    return render(request, template_name='blog/post_edit.html', context=context)


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("blog:post_list")
    return render(request, template_name='blog/post_delete.html', context={'post': post})


def page_not_found(request, exception):
    return render(request, 'blog/404.html', status=404)

def forbidden(request, exception):
    return render(request, 'blog/403.html', status=403)

def server_error(request):
    return render(request, 'blog/500.html', status=500)



