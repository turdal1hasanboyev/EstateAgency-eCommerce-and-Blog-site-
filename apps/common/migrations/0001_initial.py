# Generated by Django 5.1.2 on 2024-11-03 14:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('image', models.ImageField(default='img/default-image.jpg', upload_to='service_images')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Xizmat',
                'verbose_name_plural': 'Xizmatlar',
            },
        ),
    ]
