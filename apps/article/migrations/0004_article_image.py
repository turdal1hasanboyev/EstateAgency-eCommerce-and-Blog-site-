# Generated by Django 5.1.2 on 2024-11-04 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_article_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='img/default-image.jpg', upload_to='article_images'),
        ),
    ]