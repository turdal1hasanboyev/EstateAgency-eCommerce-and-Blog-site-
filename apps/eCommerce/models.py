from django.db import models
from ..common.models import BaseModel
from django.utils.text import slugify
from django.urls import reverse
import uuid
from ckeditor.fields import RichTextField
from apps.agent.models import Agent


class PropertyCategory(BaseModel):
    name = models.CharField(max_length=200, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, db_index=True)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Property-Kategoriya"
        verbose_name_plural = "Property-Kategoriyalar"


class Amenities(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, db_index=True)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Qulaylik/Shart-sharoit"
        verbose_name_plural = "Qulayliklar/Shart-sharoitlar"


class Property(BaseModel):
    STATUS = (
    ("In_the_living", ("In_the_living")),
    ("Sale", ("Sale")),
    ("Rent", ("Rent")),
    )
    THE_PRICE = (
        ("UZS", ("UZB")),
        ("$", ("USA")),
        ("€", ("EURO")),
        ("₽", ("RUS")),
    )
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, max_length=200, null=True, blank=True, db_index=True)
    description = RichTextField(null=True, blank=True)
    description_1 = RichTextField(null=True, blank=True)
    location = models.CharField(max_length=250)
    image = models.ImageField(upload_to='property_images/', default='img/default-image.jpg')
    video = models.FileField(upload_to='property_videos')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=225)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='property_agent')
    amenities = models.ManyToManyField(Amenities, blank=True)
    category = models.ForeignKey(to=PropertyCategory, on_delete=models.CASCADE, null=True, blank=True, related_name='property_category')
    status = models.CharField(choices=STATUS, max_length=100)
    area = models.IntegerField(default=0)
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    garages = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    is_banner = models.BooleanField(default=False)
    price_type = models.CharField(max_length=10, choices=THE_PRICE, default=("$", ("USA")))

    def get_absolute_url(self, *args, **kwargs):
        return reverse("property-single", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Mol-mulk"
        verbose_name_plural = "Mollar/Mulklar"


class PropertyImage(BaseModel):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_image')
    image = models.ImageField(upload_to='property_images')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.property.name}-{self.image}"
    
    class Meta:
        verbose_name = "PropertyRasm"
        verbose_name_plural = "PropertyRasmlari"