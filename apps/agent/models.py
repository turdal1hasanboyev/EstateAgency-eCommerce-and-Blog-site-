from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify
from ..common.models import BaseModel
import uuid


class Agent(BaseModel):
    full_name = models.CharField(max_length=155, unique=True)
    slug = models.SlugField(max_length=155, unique=True, blank=True, db_index=True)
    image = models.ImageField(upload_to='agent_images', default='img/user-default-image')
    description = RichTextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField()
    email_1 = models.EmailField(max_length=50, null=True, blank=True)
    skype = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name}"
    
    class Meta:
        verbose_name = "Agent"
        verbose_name_plural = "Agentlar"

    def get_absolute_url(self, *args, **kwargs):
        return reverse('agent-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug and self.full_name:
            self.slug = f"{slugify(self.full_name)}-{uuid.uuid4()}"
        super().save(*args, **kwargs)