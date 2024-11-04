# Generated by Django 5.1.2 on 2024-11-04 06:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=125, unique=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(default='img/user-default-image.jpg', upload_to='about_images/')),
            ],
            options={
                'verbose_name': 'Asosiy Model',
                'verbose_name_plural': 'Asosiy Modellar',
                'abstract': False,
            },
        ),
    ]