# EstateAgency-eCommerce-and-Blog-site-

1. GitHub repo ochdik
[GitHub] (https://github.com/turdal1hasanboyev/EstateAgency-eCommerce-and-Blog-site-.git)

* work.md fayl yaratdik
* README.md faylini sozladik
* .gitignore faylini sozladik
* Muhit (venv) py -m venv venv orqali yaratdik
* Muhitni faollashtirdik (venv\Scripts\activate)
* Django ni o'rnatib oldik (pip install django)
* kutubxonalarni yozib borish uchun requirements.txt faylini yaratdik (pip freeze > requirements.txt) orqali
2. Config va manage.py faylini yaratdik! (django-admin startproject config .) orqali
*Barcha buyruqlar va kutubxonalar muhit ya'ni (venv ni) ichida bajariladi*
3. Folder Structure
* (.env, .env.example, templates, media, apps, static)
* Barcha fayl va papkalarni joy joyiga qo'yib chiqish
* Barcha kerakli kutbxonalar o'rnatib olindi
```commandline
asgiref==3.8.1
Django==5.1.2
django-ckeditor==6.7.1
django-js-asset==2.2.0
django-query-counter==0.4.0
pillow==11.0.0
psycopg2-binary==2.9.10
python-environ==0.4.54
sqlparse==0.5.1
tabulate==0.9.0
tzdata==2024.2
```
* py manage.py collectstatic (statik fayllar yig'ildi birinchi marta)
* py manage.py makemigrations (migratsiyalar yaratildi)
* py manage.py migrate (migratsiyalar bajarildi)
* psql integratsiya boldi
* Custom User va Manager yozildi
4. Ertangi ishimiz 
* Malumotlar bazasi tahlili
* Custom User qayta tahlili
* Custom User admin.py tahlili
5. Modellarni birin ketin yozib chiqamiz!
# Agent
*
# Article
*
# Common
*
# Contact
*
# User
* True
# eCommerce
* 
# Custom User uchun admin.py 

```
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'id',
        'get_full_name',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'gender',
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'first_name',
        'last_name',
        'gender',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'gender',
    )
    readonly_fields = (
        'id',
        'last_login',
        "date_joined",
        'created_at',
        'updated_at',
    )
    ordering = ('id',)
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'phone_number', 'gender', 'description', 'note', 'profile_picture', 'profile_video', 'adress')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Important Dates', {
        'fields': ('created_at', 'updated_at', "date_joined", 'last_login')
        }),
    )
    add_fieldsets = (
        ('Create Super User', {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'phone_number', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
```

*Custom User models.py*
```
from django.db import models
import re
from ckeditor.fields import RichTextField
from apps.common.models import BaseModel
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    def create_user(self, email, phone_number, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not phone_number:
            raise ValueError('Users must have a phone number')
        if not re.match(r'^\+?[0-9]{10,15}$', phone_number):
            raise ValueError('Users must have a valid phone number')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not password:
            raise ValueError('Users must have a password')
        
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, phone_number, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if not email:
            raise ValueError('Users must have an email address')
        if not phone_number:
            raise ValueError('Users must have a phone number')
        if not re.match(r'^\+?[0-9]{10,15}$', phone_number):
            raise ValueError('Users must have a valid phone number')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not password:
            raise ValueError('Users must have a password')
        
        user = self.create_user(email=email, phone_number=phone_number, first_name=first_name, last_name=last_name, password=password, **extra_fields)
        return user


class CustomUser(AbstractUser, BaseModel):
    GENDER = (
        ('Erkak', ('Erkak')),
        ('Ayol', ('Ayol')),
    )
    username = None
    email = models.EmailField(unique=True)
    description = RichTextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='user_profile_pictures', default='img/user-default-image.jpg', null=True, blank=True)
    profile_video = models.FileField(upload_to='user_profile_videos', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    adress = RichTextField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
    note = models.CharField(max_length=50, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'phone_number',
        'first_name',
        'last_name',
        ]
    
    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self):
        if self.get_full_name():
            return f"{self.get_full_name()}"
        return F"{self.email}"
```