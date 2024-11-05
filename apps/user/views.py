from django.shortcuts import render, redirect
from .models import About
from ..agent.models import Agent
from ..common.models import Subscribe_Email


def login_page_view(request):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')

        Subscribe_Email.objects.create(sub_email=sub_email)
        return redirect(url)

    return render(request, 'login.html')

def about_page_view(request):
    url = request.META.get('HTTP_REFERER')

    about = About.objects.filter(is_active=True, id=1).first()
    our_team = Agent.objects.filter(is_active=True).order_by('id')[:3]

    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')

        Subscribe_Email.objects.create(sub_email=sub_email)
        return redirect(url)

    context = {
        'about': about,
        'our_team': our_team,
    }

    return render(request, 'about.html', context)