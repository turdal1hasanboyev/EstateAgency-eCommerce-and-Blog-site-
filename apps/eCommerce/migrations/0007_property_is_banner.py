# Generated by Django 5.1.2 on 2024-11-05 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerce', '0006_remove_property_image_propertyimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='is_banner',
            field=models.BooleanField(default=False),
        ),
    ]
