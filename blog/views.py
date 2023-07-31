from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, PostImageFormSet, PostImageFormSetUpdate
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import SearchForm
from functools import reduce
import operator


def search(request):
    post_list = Post.objects.none()

    query = None

    if request.method == 'GET':
        form = SearchForm(request.GET)

        if form.is_valid():
            query = form.cleaned_data['query']
            query_words = query.split()

            q_object = Q()

            for word in query_words:
                q_object |= Q(title__icontains=word) | Q(content__icontains=word)

            post_list = Post.objects.filter(q_object)

    else:
        form = SearchForm()

    paginator = Paginator(post_list, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    
    try:
        post_list  = paginator.page(page)

    except PageNotAnInteger:
        post_list = paginator.page(1)

    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    context = {
        'form': form,
        'post_list': post_list,
        'page_request_var': page_request_var,
        'query': query,
    }
    return render(request, 'search.html', context=context)


@login_required
def create_post(request):
    post_list = Post.objects.filter(status=1)
    paginator = Paginator(post_list, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    
    try:
        post_list  = paginator.page(page)

    except PageNotAnInteger:
        post_list = paginator.page(1)


    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        post_image_formset = PostImageFormSet(request.POST, request.FILES)

        if post_form.is_valid() & post_image_formset.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()

            for form in post_image_formset:
                if form.cleaned_data:
                    post_image = form.save(commit=False)
                    post_image.post = post
                    post_image.save()

            return redirect('post_detail', pk=post.pk)
        
    else:
        post_form = PostForm()
        post_image_formset = PostImageFormSet()
    
    context = {
        "post_list": post_list,
        "page_request_var": page_request_var,
        "post_form": post_form,
        "post_image_formset": post_image_formset,
    }

    return render(request, 'post_create.html', context=context)

def blog(request):
    post_list = Post.objects.filter(status=1)
    paginator = Paginator(post_list, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    
    try:
        post_list  = paginator.page(page)

    except PageNotAnInteger:
        post_list = paginator.page(1)


    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    context = {
        "post_list": post_list,
        "page_request_var": page_request_var
    }

    return render(request, 'blog.html', context=context)  

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, status=1)
    post_images = post.postimage_set.all()
    post_list = Post.objects.filter(status=1)
    paginator = Paginator(post_list, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    
    
    if request.method == 'POST':
        post.delete()
        
        return redirect('home')

    try:
        post_list  = paginator.page(page)

    except PageNotAnInteger:
        post_list = paginator.page(1)


    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    context = {
        "post_list": post_list,
        "page_request_var": page_request_var,
        'post': post,
        'post_images': post_images
    }

    return render(request, 'post_detail.html', context=context)

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post_list = Post.objects.filter(status=1)
    paginator = Paginator(post_list, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    
    try:
        post_list  = paginator.page(page)

    except PageNotAnInteger:
        post_list = paginator.page(1)


    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        post_image_formset = PostImageFormSetUpdate(request.POST, request.FILES)
        
        if post_form.is_valid() & post_image_formset.is_valid():
            post = post_form.save()

            for form in post_image_formset:
                print(form)
                if form.cleaned_data:
                    print(form)
                    post_image = form.save(commit=False)
                    post_image.post = post
                    post_image.save()
            
            return redirect('post_detail', pk=post.pk)
    
    else:
        post_form = PostForm(instance=post)
        post_image_formset = PostImageFormSetUpdate(queryset=post.postimage_set.all())
    
    context = {
        "post_list": post_list,
        "page_request_var": page_request_var,
        'post_form': post_form, 
        'post_image_formset': post_image_formset,
    }
    
    return render(request, 'post_update.html', context=context)
