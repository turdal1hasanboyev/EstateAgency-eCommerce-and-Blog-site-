from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # `CustomUser` modelini import qiling

class CustomUserAdmin(UserAdmin):
    # Admin paneldagi ustunlarni ko'rsatish uchun
    list_display = (
        'id', 
        'email', 
        'phone_number', 
        'first_name', 
        'last_name', 
        'is_active', 
        'is_staff', 
        'is_superuser', 
        'last_login', 
        'created_at',  # 'created_at' va 'updated_at' maydonlarini ko'rsatish mumkin
        'updated_at'
    )
    list_filter = ('is_staff', 'is_superuser', 'gender', 'is_active')
    search_fields = ('email', 'phone_number', 'first_name', 'last_name')

    # `CustomUser` modelida username o'rniga email ishlatilayotganligi uchun, `UserAdmin`da `USERNAME_FIELD` o'zgartirish kerak.
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': (
            'first_name', 
            'last_name', 
            'phone_number', 
            'gender', 
            'adress', 
            'description', 
            'profile_picture', 
            'profile_video')
        }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),  # 'created_at' va 'updated_at'ni olib tashladik
    )

    # Foydalanuvchi yaratishda majburiy maydonlar
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 
                'phone_number', 
                'first_name',
                'last_name',
                'description',
                'note',
                'password1', 
                'password2', 
                'is_staff', 
                'is_superuser', 
                'is_active',
            ),
        }),
    )

    ordering = ('id',)
    filter_horizontal = ()

# Admin panelda CustomUserAdmin sinfini ro'yxatdan o'tkazish
admin.site.register(CustomUser, CustomUserAdmin)