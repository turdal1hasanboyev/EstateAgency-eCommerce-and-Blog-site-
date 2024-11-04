from django.contrib import admin
from .models import Amenities, Property, PropertyCategory


class AmenitiesAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    list_display = ('id', 'name', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)
    readonly_fields = ('id', 'created_at', 'updated_at')
    prepopulated_fields = {
        'slug': ('name',)
    }


class PropertyAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'name', 'category', 'price', 'location', 'image', 'video', 'type', 'status', 'agent', 'area', 'beds', 'baths', 'garages', 'likes', 'views', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'location', 'type', 'status', 'price', 'area', 'beds', 'baths', 'garages', 'views',)
    list_filter = ('status', 'type', 'is_active', 'price', 'agent', 'category',)
    readonly_fields = ('id', 'created_at', 'updated_at',)
    prepopulated_fields = {
        'slug': ('name',)
    }

admin.site.register(Amenities, AmenitiesAdmin)
admin.site.register(Property, PropertyAdmin)


@admin.register(PropertyCategory)
class PropertyCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('id', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    ordering = ('id',)
    prepopulated_fields = {
        'slug': ('name',)
    }