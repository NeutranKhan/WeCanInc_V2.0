from blog.models import Post
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def home(request):
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

    return render(request, 'home.html', context=context)
 

def about(request):
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
    return render(request, "about.html", context=context)


def contact(request):
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
    return render(request, 'contact.html', context=context)


def projects(request):
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
    return render(request, 'projects.html', context=context)


def activities(request):
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
    return render(request, 'activities.html', context=context)


def policy(request):
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
    return render(request, "policy.html", context=context)

def donate(request):
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
    return render(request, "donate.html", context=context)
