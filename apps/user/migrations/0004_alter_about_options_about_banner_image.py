# Generated by Django 5.1.2 on 2024-11-04 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_about_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'Biz Haqimizda', 'verbose_name_plural': 'Biz Haqimizda'},
        ),
        migrations.AddField(
            model_name='about',
            name='banner_image',
            field=models.ImageField(default='img/default-image.jpg', upload_to='about_banner_images/'),
        ),
    ]