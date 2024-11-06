from django.shortcuts import render, redirect
from apps.agent.models import Agent
from ..common.models import Subscribe_Email
from ..eCommerce.models import Property


def agents_page_view(request):
    url = request.build_absolute_uri()

    agents = Agent.objects.filter(is_active=True).order_by('-id')[:6]

    if request.method == 'POST':
        sub_email = Subscribe_Email()
        sub_email.sub_email = request.POST.get('sub_email')
        sub_email.save()
        return redirect(url)

    return render(request, 'agents-grid.html', context={'agents': agents})

def agent_single_page_view(request, slug):
    # url = request.META.get('HTTP_REFERER') # Oldingi sahifani qaytaradi
    url = request.build_absolute_uri() # Hozirgi sahifani qaytaradi

    agent = Agent.objects.filter(is_active=True, slug__exact=slug).first()
    my_properties = Property.objects.filter(is_active=True, agent_id=agent.id).order_by('id')[:6]

    if request.method == 'POST':
        sub_email = Subscribe_Email()
        sub_email.sub_email = request.POST.get('sub_email')
        sub_email.save()
        return redirect(url)

    context = {
        'agent': agent,
        'my_properties': my_properties,
    }

    return render(request=request, template_name='agent-single.html', context=context)