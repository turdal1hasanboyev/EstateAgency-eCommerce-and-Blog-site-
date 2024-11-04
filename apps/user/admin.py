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