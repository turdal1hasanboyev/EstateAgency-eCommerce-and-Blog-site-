# Generated by Django 5.1.2 on 2024-11-05 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerce', '0008_property_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='price_type',
            field=models.CharField(choices=[('UZS', 'UZB'), ('$', 'USA'), ('€', 'EURO'), ('₽', 'RUS')], default=0, max_length=10),
            preserve_default=False,
        ),
    ]