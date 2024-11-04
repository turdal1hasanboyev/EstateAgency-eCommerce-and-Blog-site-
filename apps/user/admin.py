from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, About


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


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'id',                # Foydalanuvchining ID raqami
        'name',              # Nomi
        'image',             # Rasm
        'is_active',         # Foydalanuvchining faol holati
        'created_at',        # Yaratilgan sanasi
        'updated_at',        # Yangilangan sanasi
    )
    
    ordering = ('-id',)  # ID ga qarab tartiblash
    search_fields = ('name',)      # Qidiruv maydoni
    list_filter = ('is_active', 'name',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )