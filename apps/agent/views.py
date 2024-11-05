from django.shortcuts import render
from apps.agent.models import Agent


def agents_page_view(request):

    context = {

    }

    return render(request, 'agents-grid.html', context)

def agent_single_page_view(request, slug):
    agent = Agent.objects.filter(is_active=True, slug__exact=slug).first()

    context = {
        'agent': agent,
    }

    return render(request=request, template_name='agent-single.html', context=context)