# Generated by Django 5.1.2 on 2024-11-04 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0004_agent_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='agent',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
