# Generated by Django 5.1.2 on 2024-11-05 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerce', '0009_property_price_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price_type',
            field=models.CharField(choices=[('UZS', 'UZB'), ('$', 'USA'), ('€', 'EURO'), ('₽', 'RUS')], default=('$', 'USA'), max_length=10),
        ),
    ]
