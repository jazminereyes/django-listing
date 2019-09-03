# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Blog, Product, Inquiry
from .forms import BlogForm, SignUpForm, ProductForm, InquiryForm

# Create your views here.
def index(request):
    return render(request, 'listing/index.html')

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else: 
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def get_recent():
    recent = Blog.objects.order_by('-created_at')[:3]
    return recent

def blog(request):
    if request.method == "POST":
        result = Blog.objects.filter(
            Q(title__icontains=request.POST['search']) | Q(content__icontains=request.POST['search'])
        )

        paginator = Paginator(result, 5)

        page = request.GET.get('page')

        try:
            blog = paginator.page(page)
        except PageNotAnInteger:
            blog = paginator.page(1)
        except EmptyPage:
            blog = paginator.page(paginator.num_pages)

        context = {
            'blog': blog,
            'result': result,
            'text': request.POST['search'],
            'recent': get_recent()
        }
    else:
        blog_list = Blog.objects.all()
        paginator = Paginator(blog_list, 5)

        page = request.GET.get('page')

        try:
            blog = paginator.page(page)
        except PageNotAnInteger:
            blog = paginator.page(1)
        except EmptyPage:
            blog = paginator.page(paginator.num_pages)

        context = {
            'blog': blog,
            'recent': get_recent()
        }
    return render(request, 'listing/blog.html', context)

def blog_view(request, blog_id):
    blog_single = Blog.objects.get(pk=blog_id)
    context = {
        'blog_single': blog_single,
        'recent': get_recent()
    }
    return render(request, 'listing/blog-single.html', context)

@login_required
def blog_user(request, user_id):
    blog_list = Blog.objects.filter(author=user_id)
    paginator = Paginator(blog_list, 5)

    page = request.GET.get('page')

    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)

    context = {
        'blog': blog,
        'recent': get_recent()
    }
    return render(request, 'listing/blog-user.html', context)

@login_required
def blog_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user 
            article.save()
            return redirect('blog')
    else:
        form = BlogForm()
    return render(request, 'listing/blog-detail.html', {'form': form})

@login_required
def blog_edit(request, blog_id):
    article = Blog.objects.get(pk=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user 
            article.save()
            return redirect('blog_view', blog_id=article.pk)
    else:
        form = BlogForm(instance=article)
    return render(request, 'listing/blog-detail.html', {'form': form})

@login_required 
def blog_remove(request, blog_id):
    article = Blog.objects.get(pk=blog_id)
    article.delete()
    return redirect('blog')

def shop(request):
    if request.method == "POST":
        result = Product.objects.filter(
            Q(product_name__icontains=request.POST['product']) | Q(product_description__icontains=request.POST['product'])
        )
        paginator = Paginator(result, 12)
        page = request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context = {
            'products': products,
            'text': request.POST['product'],
            'result': result
        }
    else:
        products_list = Product.objects.all()
        paginator = Paginator(products_list, 12)

        page = request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context = {
            'products': products
        }
    return render(request, 'listing/shop.html', context)

def shop_view(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'listing/shop-single.html', context)

@login_required
def shop_user(request, user_id):
    products_list = Product.objects.filter(user=user_id)
    paginator = Paginator(products_list, 12)

    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products
    }
    return render(request, 'listing/shop-user.html', context)

@login_required
def shop_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user 
            product.save()
            return redirect('shop')
    else:
        form = ProductForm()
    return render(request, 'listing/shop-detail.html', {'form': form})

@login_required
def shop_edit(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user 
            product.save()
            return redirect('shop_view', product_id=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'listing/shop-detail.html', {'form': form})

@login_required 
def shop_remove(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('shop')

def inquiry(request):
    if request.method == "POST":
        result = Inquiry.objects.filter(
            Q(title__icontains=request.POST['inquiry']) | Q(question__icontains=request.POST['inquiry'])
        )

        paginator = Paginator(result, 12)
        page = request.GET.get('page')

        try:
            inquiries = paginator.page(page)
        except PageNotAnInteger:
            inquiries = paginator.page(1)
        except EmptyPage:
            inquiries = paginator.page(paginator.num_pages)

        context = {
            'inquiries': inquiries,
            'text': request.POST['inquiry'],
            'result': result
        }
    else:
        inquiry_list = Inquiry.objects.all()
        paginator = Paginator(inquiry_list, 12)
        page = request.GET.get('page')

        try:
            inquiries = paginator.page(page)
        except PageNotAnInteger:
            inquiries = paginator.page(1)
        except EmptyPage:
            inquiries = paginator.page(paginator.num_pages)

        context = {
            'inquiries': inquiries
        }
    return render(request, 'listing/inquiry.html', context)

def inquiry_view(request, inquiry_id):
    inquiry = Inquiry.objects.get(pk=inquiry_id)
    context = {
        'inquiry': inquiry,
    }
    return render(request, 'listing/inquiry-single.html', context)

@login_required
def inquiry_user(request, user_id):
    inquiry_list = Inquiry.objects.filter(author=user_id)
    paginator = Paginator(inquiry_list, 5)

    page = request.GET.get('page')

    try:
        inquiries = paginator.page(page)
    except PageNotAnInteger:
        inquiries = paginator.page(1)
    except EmptyPage:
        inquiries = paginator.page(paginator.num_pages)

    context = {
        'inquiries': inquiries
    }
    return render(request, 'listing/inquiry-user.html', context)

@login_required
def inquiry_new(request):
    if request.method == "POST":
        form = InquiryForm(request.POST, request.FILES)

        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.author = request.user 
            inquiry.save()
            return redirect('inquiry')
    else:
        form = InquiryForm()
    return render(request, 'listing/inquiry-detail.html', {'form': form})

@login_required
def inquiry_edit(request, inquiry_id):
    inquiry = Inquiry.objects.get(pk=inquiry_id)
    if request.method == "POST":
        form = InquiryForm(request.POST, instance=inquiry)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.author = request.user 
            inquiry.save()
            return redirect('inquiry_view', inquiry_id=inquiry.pk)
    else:
        form = InquiryForm(instance=inquiry)
    return render(request, 'listing/inquiry-detail.html', {'form': form})

@login_required 
def inquiry_remove(request, inquiry_id):
    inquiry = Inquiry.objects.get(pk=inquiry_id)
    inquiry.delete()
    return redirect('inquiry')