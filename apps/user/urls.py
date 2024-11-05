from django.urls import path
from .views import login_page_view, about_page_view


urlpatterns = [
    path('login/', login_page_view, name="login"),
    path('about/', about_page_view, name="about"),
]