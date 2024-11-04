from django.contrib import admin
from .models import Agent


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = (
        'id',                 # Agentning ID raqami
        'full_name',          # Agentning to'liq ismi
        'image',              # Agentning rasmi
        'phone_number',       # Agentning telefon raqami
        'mobile_number',      # Agentning mobil raqami
        'email',              # Agentning email manzili
        'email_1',            # Agentning ikkinchi email manzili
        'skype',              # Agentning Skype manzili
        'type',               # Agent turini ko'rsatadi
        'is_active',          # Faol holati
        'created_at',         # Yaratilgan sanasi
        'updated_at',         # Yangilangan sanasi
    )

    ordering = ('-created_at',)  # Yaratilgan sanaga qarab tartiblash
    search_fields = ('full_name', 'email', 'type', 'skype', 'email_1', 'phone_number', 'mobile_number')  # Qidiruv maydonlari
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'type',
        'phone_number',
        'email',
    )
    prepopulated_fields = {"slug": ["full_name",]}