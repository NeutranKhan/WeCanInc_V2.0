from blog.models import Post
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def get_involve(request):
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
    return render(request, 'get_involve.html', context=context)


def volunteer(request):
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
    return render(request, "volunteer.html", context=context)

def volunteer_form(request):
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
    return render(request, "volunteer_form.html", context=context)

def join_us(request):
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
    return render(request, "join_us.html", context=context)

def join_us_form(request):
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
    return render(request, "join_us_form.html", context=context)

