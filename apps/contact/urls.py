from django.urls import path
from .views import contact_page_view


urlpatterns = [
    path('contact/', contact_page_view, name="contact"),
]