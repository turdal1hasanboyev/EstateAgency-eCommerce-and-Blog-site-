from django.contrib import admin
from .models import Agent


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'gender',
        'image',
        'phone_number',
        'mobile_number',
        'email',
        'email_1',
        'views',
        'likes',
        'skype',
        'type',
        'is_active',
        'created_at',
        'updated_at',
    )

    ordering = ('-created_at',)
    search_fields = ('full_name', 'email', 'type', 'skype', 'email_1', 'phone_number', 'mobile_number', 'gender',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'type',
        'full_name',
        'skype',
        'gender',
    )
    prepopulated_fields = {"slug": ["full_name",]}