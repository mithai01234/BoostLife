from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from rest_framework import generics
from .models import Article
from .serializers import ImageInfoSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
@permission_classes([IsAuthenticated])
class ImageInfoList(generics.ListAPIView):
    queryset = Article.objects.filter(status=True).order_by('-id')
    serializer_class = ImageInfoSerializer
@permission_classes([IsAuthenticated])
class ImageInfoListFive(generics.ListAPIView):
    queryset = Article.objects.filter(status=True).order_by('-id')[:5]
    serializer_class = ImageInfoSerializer
@login_required(login_url='backend/login')
def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'backend/article_list.html', context)

@login_required(login_url='backend/login')
def article_add(request):
    if request.method == "POST":
        article = Article()
        name = request.POST.get('name')
        image = request.FILES.get('image')
        article.name = name
        article.image = image
        article.save()
        return redirect('article_list')
    return render(request, 'backend/article_add.html')

@login_required(login_url='backend/login')
def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('article_list')

@login_required(login_url='backend/login')
def article_edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {
        'article': article
    }
    return render(request, 'backend/article_edit.html', context)

@login_required(login_url='backend/login')
def article_update(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        article.name = request.POST.get('name')
        if request.FILES.get('image'):
            article.image = request.FILES.get('image')
        article.save()
        return redirect('article_list')
    return render(request, 'backend/article_edit.html', {'article': article})

@login_required(login_url='backend/login')
def activate_article(request, product_id):
    banner = get_object_or_404(Article, id=product_id)
    banner.status = True
    banner.save()
    return redirect('article_list')  # Redirect to your banner list view

@login_required(login_url='backend/login')
def deactivate_article(request, product_id):
    banner = get_object_or_404(Article, id=product_id)
    banner.status = False
    banner.save()
    return redirect('article_list')  # Redirect to your banner list view