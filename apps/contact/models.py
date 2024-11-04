from django.db import models
from ..common.models import BaseModel
from ckeditor.fields import RichTextField


class Contact(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=125)
    message = RichTextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Biz bilan aloqa"
        verbose_name_plural = "Biz bilan aloqa"  # noqa: E501

class AgentContact(BaseModel):
    name = models.CharField(max_length=155)
    agent = models.ForeignKey('agent.Agent', on_delete=models.CASCADE, related_name="AgentContact")
    email = models.EmailField()
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.agent}"
    
    class Meta:
        verbose_name = "Agent bilan aloqa"
        verbose_name_plural = "Agent bilan aloqa"  # noqa: E501