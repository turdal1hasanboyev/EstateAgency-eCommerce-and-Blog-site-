from django.contrib import admin
from .models import Service, Testimonial, Country, Company, Liked, Subscribe_Email


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('id',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_testimonial_full_name',
        'male_name',
        'female_name',
        'image',
        'video',
        'views',
        'likes',
        'is_active',
        'created_at',
        'updated_at',
    )
    
    ordering = ('-created_at',)
    search_fields = ('male_name', 'female_name')
    list_filter = ('is_active', 'male_name', 'female_name')
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'title', 'link', 'created_at', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('id', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'title', 'link', 'created_at', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('id', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Liked)
class LikedAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'from_user',
        'agent',
        'liked_agent',
        'article',
        'liked_article',
        'comment',
        'liked_comment',
        'testimonial',
        'liked_testimonial',
        'property',
        'liked_property',
        'user',
        'liked_user',
        'is_active',
        'created_at',
        'updated_at'
    )
    ordering = ('-id',)
    search_fields = ('from_user__first_name',) ## Ichma ich kirish
    list_filter = ('is_active',)
    readonly_fields = ('id', 'created_at', 'updated_at')


@admin.register(Subscribe_Email)
class SubscribeEmailAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'sub_email', 'created_at', 'updated_at')
    search_fields = ('sub_email',)
    list_filter = ('is_active',)
    readonly_fields = ('id', 'created_at', 'updated_at')