# Generated by Django 5.1.2 on 2024-11-05 03:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerce', '0005_property_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='image',
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='property_images')),
                ('is_main', models.BooleanField(default=False)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_image', to='eCommerce.property')),
            ],
            options={
                'verbose_name': 'PropertyRasm',
                'verbose_name_plural': 'PropertyRasmlari',
            },
        ),
    ]
