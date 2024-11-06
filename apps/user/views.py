from django.shortcuts import render, redirect
from .models import About
from ..agent.models import Agent
from ..common.models import Subscribe_Email
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser


def register_page_view(request):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')

        Subscribe_Email.objects.create(sub_email=sub_email)
        return redirect(url)

    if request.method == 'POST':
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, "Parollar bir xil emas.")
            return render(request, 'register.html')

        try:
            # Foydalanuvchini yaratishda `create_user` metodidan foydalanamiz
            user = CustomUser.objects.create_user(
                email=email,
                phone_number=phone_number,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            messages.success(request, "Akkount muvaffaqiyatli yaratildi!")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Xato: {e}")
            return render(request, 'register.html')

    return render(request, 'register.html')

def login_page_view(request):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')

        Subscribe_Email.objects.create(sub_email=sub_email)
        return redirect(url)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')  # `home` sahifasiga yo‘naltirish
        else:
            messages.error(request, "Login yoki parol noto'g'ri. Qayta urinib ko'ring.")
            return render(request, 'login.html')

    return render(request, 'login.html')

@login_required
def logout_page_view(request):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')

        Subscribe_Email.objects.create(sub_email=sub_email)
        return redirect(url)
    
    logout(request)
    return redirect('/')

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