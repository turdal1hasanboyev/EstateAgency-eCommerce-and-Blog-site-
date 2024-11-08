# Generated by Django 5.1.2 on 2024-11-04 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('link', models.URLField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Asosiy Model',
                'verbose_name_plural': 'Asosiy Modellar',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='country',
            name='link',
            field=models.URLField(default=0, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='slug',
            field=models.SlugField(blank=True, max_length=55, null=True, unique=True),
        ),
    ]
