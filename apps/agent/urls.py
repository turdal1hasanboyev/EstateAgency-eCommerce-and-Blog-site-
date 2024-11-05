from django.urls import path
from . import views


urlpatterns = [
    path('agents_grid/', views.agents_page_view, name='agents'),
    path('agent_detail/<slug:slug>/', views.agent_single_page_view, name='agent-single'),
]