from django.contrib import admin
from .models import Service, Testimonial


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description_snippet', 'image_preview', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'created_at', 'updated_at')
    readonly_fields = ('id','image_preview', 'created_at', 'updated_at')

    def description_snippet(self, obj):
        # description maydonining qisqa ko‘rinishini qaytaradi
        return obj.description[:50] + '...' if obj.description else 'No description'
    description_snippet.short_description = 'Description'

    def image_preview(self, obj):
        # Admin panelda rasmning kichik ko'rinishini hosil qiladi
        if obj.image:
            return f'<img src="{obj.image.url}" style="width: 50px; height:50px;" />'
        return "No Image"
    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'id',               # Foydalanuvchining ID raqami
        'male_name',       # Erkak ismi
        'female_name',     # Ayol ismi
        'testimonial',     # Guvohnoma matni
        'image',           # Guvohnoma rasmi
        'is_active',       # Foydalanuvchining faol holati
        'created_at',      # Yaratilgan sanasi
        'updated_at',      # Yangilangan sanasi
    )
    
    # Bu yerda modelni tartiblash bo'yicha ko'rsatmalar berilishi mumkin
    ordering = ('-created_at',)  # Yangilanish sanasiga qarab tartiblash
    search_fields = ('male_name', 'female_name')  # Qidiruv maydonlari
    list_filter = ('is_active', 'male_name', 'female_name')
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )