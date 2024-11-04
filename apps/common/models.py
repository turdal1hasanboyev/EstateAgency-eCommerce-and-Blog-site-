from django.db import models
from ckeditor.fields import RichTextField


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

    def __str__(self):
        return f"{self.male_name} - {self.female_name}"
    
    class Meta:
        verbose_name = "Guvohnoma"
        verbose_name_plural = "Guvohnomalar"