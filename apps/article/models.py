from django.db import models
from ..common.models import BaseModel
from ckeditor.fields import RichTextField
import uuid
from django.utils.text import slugify
from django.urls import reverse
from apps.user.models import CustomUser


class ArticleCategory(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, db_index=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Maqola Kategoriyasi"
        verbose_name_plural = "Maqola Kategoriyalari"
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"
        super().save(*args, **kwargs)


class ArticleTag(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, db_index=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Maqola HashTagi"
        verbose_name_plural = "Maqola HashTaglari"
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Article(BaseModel):
    title = models.CharField(max_length=250, unique=True)
    sub_title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, db_index=True, null=True, blank=True, unique=True)
    category = models.ForeignKey(to=ArticleCategory, on_delete=models.CASCADE, related_name="ArticleCategory")
    tags = models.ManyToManyField(to=ArticleTag, blank=True)
    author = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name="ArticleAuthor")
    description = RichTextField(null=True, blank=True)
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("article-single", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = f"{slugify(self.title)}-{uuid.uuid4()}"
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"
    

class Comment(BaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="CommentArticle")
    user = models.ForeignKey("user.CustomUser", on_delete=models.SET_NULL, null=True, related_name='CommentUser')
    name = models.CharField(max_length=225)
    email = models.EmailField()
    web_site = models.URLField()
    comment = RichTextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user}-{self.article}"
    
    class Meta:
        verbose_name = "Maqola Komentariyasi"
        verbose_name_plural = "Maqola Komentariyalari"