# Generated by Django 5.1.2 on 2024-11-05 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_customuser_likes_customuser_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
