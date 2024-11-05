from django.urls import path
from .views import home_page_view, property_single_page_view, properties_page_view


urlpatterns = [
    path('', home_page_view, name='home'),
    path('property-single/<slug:slug>/', property_single_page_view, name="property-single"),
    path('properties/', properties_page_view, name="properties"),
]