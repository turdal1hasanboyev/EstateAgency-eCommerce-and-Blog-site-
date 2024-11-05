from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from uuid import uuid4


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "Asosiy Model"
        verbose_name_plural = "Asosiy Modellar"


class Service(BaseModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    image = models.ImageField(upload_to='service_images', default='img/default-image.jpg')
    description = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name = "Xizmat"
        verbose_name_plural = "Xizmatlar"

    def __str__(self):
        return f"{self.name}"
    

class Testimonial(BaseModel):
    male_name = models.CharField(max_length=100)
    female_name = models.CharField(max_length=100)
    testimonial = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='testimonials/', default='img/default-image.jpg')
    video = models.FileField(upload_to='testimonial_videos')
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.male_name} - {self.female_name}"
    
    def get_testimonial_full_name(self):
        return f"{self.male_name} & {self.female_name}"
    
    class Meta:
        verbose_name = "Guvohnoma"
        verbose_name_plural = "Guvohnomalar"


class Country(BaseModel):
    title = models.CharField(max_length=55, unique=True)
    slug = models.SlugField(max_length=55, unique=True, null=True, blank=True, db_index=True)
    link = models.URLField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Mamlakat"
        verbose_name_plural = "Mamlakatlar"


class Company(BaseModel):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True, db_index=True)
    link = models.URLField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = f"{slugify(self.title)}-{uuid4()}"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Kompaniya"
        verbose_name_plural = "Kompaniyalar"


class Liked(BaseModel):
    LIKED = (
        ('Like', ('Like')),
        ('Dislike', ('Dislike')),
    )
    from_user = models.ForeignKey(to='user.CustomUser', on_delete=models.CASCADE, related_name='liked_from_user')
    agent = models.ForeignKey(to='agent.Agent', on_delete=models.CASCADE, related_name='liked_agent')
    liked_agent = models.CharField(max_length=15, choices=LIKED, default=('Like', ('Like')))
    article = models.ForeignKey('article.Article', on_delete=models.CASCADE, related_name='liked_article')
    liked_article = models.CharField(max_length=15, choices=LIKED, default=('Like', ('Like')))
    comment = models.ForeignKey('article.Comment', on_delete=models.CASCADE, related_name='liked_comment')
    liked_comment = models.CharField(max_length=15, choices=LIKED, default=('Like', ('Like')))
    testimonial = models.ForeignKey('common.Testimonial', on_delete=models.CASCADE, related_name='liked_testimonial')
    liked_testimonial = models.CharField(max_length=15, choices=LIKED, default=('Like', ('Like')))
    property = models.ForeignKey('eCommerce.Property', on_delete=models.CASCADE, related_name='liked_property')
    liked_property = models.CharField(max_length=15, choices=LIKED, default=('Like', ('Like')))
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='liked_user')
    liked_user = models.CharField(max_length=15, choices=LIKED, default=('Like', ('Like')))

    def __str__(self):
        return f"{self.from_user}"
    
    class Meta:
        verbose_name = "Yoqtirish"
        verbose_name_plural = "Yoqtirishlar"


class Subscribe_Email(BaseModel):
    sub_email = models.EmailField(unique=True, max_length=100)

    def __str__(self):
        return f"{self.sub_email}"
    
    class Meta:
        verbose_name = "EmailObuna"
        verbose_name_plural = "EmailObunalar"