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
* Modellarni birin ketin yozib chiqamiz!
# Agent
* True
# Article
* True
# Common
* True
# Contact
* True
# User
* True
# eCommerce
* True
# Custom User uchun admin.py 
* True
```
user.admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, About


admin.site.site_header = "Estate Agency Admin Paneli"
admin.site.site_title = "Estate Agency Admin Paneli"
admin.site.index_title = "Estate Agency Boshqaruv Paneliga Xush Kelibsiz!"


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
        'profile_picture',
        'profile_video',
        'views',
        'likes',
        'birth_date',
        'age',
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
        'age',
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
            'fields': ('first_name', 'last_name', 'phone_number', 'gender', 'description', 'note', 'profile_picture', 'profile_video', 'adress',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Important Dates', {
        'fields': ('created_at', 'updated_at', "date_joined", 'last_login', 'birth_date', 'age',)
        }),
    )
    add_fieldsets = (
        ('Create Super User', {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'phone_number', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'banner_image',
        'image',
        'is_active',
        'created_at',
        'updated_at',
    )
    
    ordering = ('-id',)
    search_fields = ('name',)
    list_filter = ('is_active', 'name',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
```
*user.models.py*
```
from django.db import models
import re
from ckeditor.fields import RichTextField
from apps.common.models import BaseModel
from django.contrib.auth.models import AbstractUser, UserManager
from datetime import date


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
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    birth_date = models.DateField(null=True, blank=True)

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
    
    def age(self):
        # Agar birth_date mavjud emas yoki noto‘g‘ri formatda bo‘lsa, None qaytaramiz
        if not isinstance(self.birth_date, date):
            return None

        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age
    

class About(BaseModel):
    name = models.CharField(max_length=125, unique=True)
    description = RichTextField(null=True, blank=True)
    banner_image = models.ImageField(upload_to='about_banner_images/', default='img/default-image.jpg')
    image = models.ImageField(upload_to='about_images/', default='img/user-default-image.jpg')

    class Meta:
        verbose_name = 'Biz Haqimizda'
        verbose_name_plural = 'Biz Haqimizda'

    def __str__(self):
        return f"{self.name}"
```
# Men ertaga nima ish qilaman?
* Bugun barcha modellar deyarli tarzda yozib bo'lindi lekin umumiy ravishda qayta tekshiruv bo'lishi kerak
* Har bir app va har bir model va adminka qismi qayta tekshiruvdan otadi
# Admin panel ga alohida etibor
* Ertaga template ham yozamiz
# Barcha modellar yozib bo'lindi
# Liked (Agent, Article, Comment, Testimonial, Property, User)
* Model yozish tugadi!!!
5. Bugungi ishimiz template, views, urls larni yozish

```
admin.site.site_header = "Estate Agency Admin Paneli"
admin.site.site_title = "Estate Agency Admin Paneli"
admin.site.index_title = "Estate Agency Boshqaruv Paneliga Xush Kelibsiz!"
```
* Admin sahifa nomini o'zgartirish usuli
```
@admin.register(Your Model) - adminni to'g'ridan to'g'ri class bilan registratsiya qilish
class YouModelAdmin(admin.ModelAdmin):
...
...
admin.site.register(YourModel, YouModelAdmin) - oldin admin class admin yaratib model va modeladminni yonma yon register qilish
class YouModelAdmin(admin.ModelAdmin):
...
...
ModelAdmin - oddiy modellar uchun
UserAdmin - odatda CustomUser modellari uchun
Fieldlari
ordering - tartiblash
list_display - displayda korinadigan fieldlarini tartib bilan yozib chiqish
list_filter - listda filterlash berilgan fieldlar bo'yicha
search_fields - qidiruv tizimi berilgan fieldlar bo'yicha (fieldlar ichiga ichma ich kirish __ bilan)
readonly_fields - faqat o'qisa boladigan fieldlar
inlines = [your inline class(model)] - inline qo'shish
prepopulated_fields = {
        'slug': ('title',)
    } - avtomatik to'ldiriladigan fieldlar ushbu ko'rinishda yoziladi
Oltin qoida! fieldlar odatda () ichiga yoziladi va oxirgi field dan so'ng , qo'yish kerak
```
* Adminkada Inlines qo'shamiz
* Admin panelda qanday qilib inline qo'shishni ko'rdik
```
# models.py (Propertyda image fildi kerak emas)
class PropertyImage(BaseModel):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_image')
    image = models.ImageField(upload_to='property_images')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.property.name}-{self.image}"
    
    class Meta:
        verbose_name = "PropertyRasm"
        verbose_name_plural = "PropertyRasmlari"
```
```
# property adminida inline orqali ushbu klass nomi yozilsin
Bu klass ni alohida royhatdan otkazish shart emas
class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 0
```
* Tugilgan kun kiritilganda bugun necha yoshligimni aniqlab beradigan qilish
# app name ishlatmaslik kerak ekan get_absolute_url da hato boryapti
Contact va blog pagelarni qilamiz
About modelni tekshiramiz
```
Comments ({{ article.CommentArticle.count }}) article ga yozilgan Izohlar sonini chiqarish
Diqqat qoida article bu hozirgi paytdagi obyekt
CommentArticle esa Comment klass ning articlega ulangandagi related name i
related name berilgan bolsa <obyekt>.<related_name>.count
aks holda <hozirgi obyekt>.<klass nomi>_set.count tarzida beriladi
```
```
{{ article.comment_set.count }} bu usulim ishlamdi
ChatGPT сказал:
ChatGPT
{{ article.comment_set.count }} Django Template Templatedagi comment_set ni ishlamagan bo'lsa, bir necha sabablarga ko'ra bo'lishi mumkin. Keling, muammolarni aniqlash uchun ba'zi tekshiruvlarni amalga oshiramiz:

Modellar O‘rtasidagi Aloqa: article modelida Comment modeli bilan ForeignKey aloqasi borligiga ishonch hosil qiling. Masalan:

python
Копировать код
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
Bu yerda related_name="comments" belgilangan, shunda article.comments.count sifatida comment_set o'rniga foydalanish mumkin.

related_nameni Tekshirish: Agar ForeignKey ga related_name qo‘llagan bo‘lsangiz, comment_set o‘rniga bu nomni ishlatishingiz kerak bo‘ladi. Masalan:

html
Копировать код
{{ article.comments.count }}
Bo'sh Ma'lumot: Comment modelida hech qanday yozuv yo‘qligiga ishonch hosil qiling, ya'ni comment_set mavjud bo'lmasligi mumkin.

Admin Panelda Tekshirish: Comment modelingizda Article ga bog'langan yozuvlar borligiga va ular to'g'ri ishlayotganiga ishonch hosil qiling.

Agar yuqoridagi qadamlar ish bermasa yoki qo‘shimcha yordam kerak bo‘lsa, menga xabar bering!
```
* Ertaga agent app ni koramiz template yozamiz loyihani qaytadan tahlil qilamiz