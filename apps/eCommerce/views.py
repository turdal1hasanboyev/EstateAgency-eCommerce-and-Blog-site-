from django.shortcuts import render, get_object_or_404, redirect
from apps.eCommerce.models import Property
from apps.common.models import Service
from apps.agent.models import Agent
from apps.article.models import Article
from ..common.models import Testimonial, Subscribe_Email
from apps.contact.models import AgentContact


def home_page_view(request):
    url = request.META.get('HTTP_REFERER')

    banners = Property.objects.filter(is_active=True, is_banner=True).order_by('-id')[:3]
    our_services = Service.objects.filter(is_active=True).order_by('name')[:3]
    latest_properties = Property.objects.filter(is_active=True).order_by('-id')[:4]
    best_agents = Agent.objects.filter(is_active=True).order_by('full_name')[:3]
    latest_news = Article.objects.filter(is_active=True).order_by('-id')[:4]
    testimonials = Testimonial.objects.filter(is_active=True).order_by('?')[:2]

    context = {
        'banners': banners,
        'our_services': our_services,
        'latest_properties': latest_properties,
        'best_agents': best_agents,
        'latest_news': latest_news,
        'testimonials': testimonials,
    }
    
    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')
        
        Subscribe_Email.objects.create(sub_email=sub_email)
        return redirect(url)

    return render(request, 'home.html', context)

def property_single_page_view(request, slug):
    url = request.META.get('HTTP_REFERER')

    property = get_object_or_404(Property, slug__iexact=slug, is_active=True)
    property.views +=1
    property.save()

    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')

        sub_email = Subscribe_Email.objects.create(sub_email=sub_email)
        sub_email.save()
        return redirect(url)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("comment")

        AgentContact.objects.create(
            agent_id=property.agent.id,
            name=name,
            email=email,
            comment=comment,
        )
        return redirect(url)

    return render(request=request, template_name='property-single.html', context={'property': property})

def properties_page_view(request):
    properties = Property.objects.filter(is_active=True).order_by('?')[:6]

    if request.method == 'POST':
        sub_email = Subscribe_Email()
        sub_email.sub_email = request.POST.get('sub_email')
        sub_email.save()
        return redirect('properties')

    return render(request, 'properties-grid.html', {'properties': properties})