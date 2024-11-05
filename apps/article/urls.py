from django.urls import path
from .views import blogs_page_view, blog_detail_page_view


urlpatterns = [
    path('articles/', blogs_page_view, name='article'),
    path('article-single/<slug:slug>/', blog_detail_page_view, name='article-single'),
]