from django.contrib import admin
from .models import Contact, AgentContact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'is_active',
        'created_at',
        'updated_at',
    )
    
    ordering = ('-name',) 
    search_fields = ('name',)
    list_filter = (
        'name',
        'email',
        'is_active',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )


@admin.register(AgentContact)
class AgentContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'agent',
        'name',
        'email',
        'is_active',
        'created_at',
        'updated_at',
    )
    
    ordering = ('id',) 
    search_fields = ('name', 'agent')
    list_filter = (
        'agent',
        'name',
        'email',
        'is_active',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )