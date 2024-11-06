from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from apps.common.models import Subscribe_Email


def blogs_page_view(request):
    articles = Article.objects.filter(is_active=True).order_by('id')[:6]

    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')

        Subscribe_Email.objects.create(sub_email=sub_email)
        return redirect('article')

    return render(request, 'blogs-grid.html', context={'articles': articles})

def blog_detail_page_view(request, slug):
    url = request.META.get('HTTP_REFERER')

    article = get_object_or_404(Article, is_active=True, slug__iexact=slug)
    comments = Comment.objects.filter(is_active=True, article_id=article.id).order_by('-id')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        web_site = request.POST.get('web_site')
        comment = request.POST.get('comment')

        Comment.objects.create(
            article_id=article.id,
            user_id=request.user.id,
            name=name,
            email=email,
            web_site=web_site,
            comment=comment,
            views=0,
            likes=0,
        )
        return redirect('article-single', article.slug)
    
    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')
        
        Subscribe_Email.objects.create(sub_email=sub_email)
        return redirect(url)

    context = {
        'article': article,
        'comments': comments,
    }

    return render(request, 'blog-single.html', context)