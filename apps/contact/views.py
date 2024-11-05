from django.shortcuts import render, redirect
from .models import Contact
from ..common.models import Subscribe_Email


def contact_page_view(request):
    url = request.META.get('HTTP_REFERER')

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            user_id=request.user.id,
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        return redirect(url)
    
    if request.method == 'POST':
        sub_email = Subscribe_Email()
        sub_email.sub_email = request.POST.get('sub_email')
        sub_email.save()
        return redirect(url)

    return render(request, 'contact.html')