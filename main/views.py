from django.shortcuts import render,redirect
from django.contrib import messages
from .models import News, Category

def home(request):
    featured_news=News.objects.last()
    three_news=News.objects.all()[0:3]
    three_categories=Category.objects.all()[0:3]
    return render(request,'home.html',{
        'featured_news':featured_news,
        'three_news':three_news,
        'three_categories':three_categories
    })

def detail(request,id):
    news=News.objects.get(pk=id)
    category=Category.objects.get(id=news.category.id)
    rel_news=News.objects.filter(category=category).exclude(id=id)
    return render(request,'detail.html',{
        'news':news,
        'related_news':rel_news,
        'category':category
    })

def category(request,id):
    category=Category.objects.get(id=id)
    news=News.objects.filter(category=category)
    return render(request,'category-news.html',{
        'all_news':news,
        'category':category
    })

