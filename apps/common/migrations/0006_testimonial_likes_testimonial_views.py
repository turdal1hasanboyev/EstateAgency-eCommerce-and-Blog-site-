# Generated by Django 5.1.2 on 2024-11-04 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_company_options_alter_country_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
