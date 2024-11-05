from django.shortcuts import render, get_object_or_404
from .models import Article


def blogs_page_view(request):
    context = {

    }

    return render(request, 'blogs-grid.html', context)

def blog_detail_page_view(request, slug):
    article = get_object_or_404(Article, is_active=True, slug__iexact=slug)

    context = {
        'article': article,
    }

    return render(request, 'blog-single.html', context)