from django.db import models
from ckeditor.fields import RichTextField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

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