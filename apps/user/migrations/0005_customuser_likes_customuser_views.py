# Generated by Django 5.1.2 on 2024-11-04 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_about_options_about_banner_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
