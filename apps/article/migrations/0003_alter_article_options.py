# Generated by Django 5.1.2 on 2024-11-04 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Maqola', 'verbose_name_plural': 'Maqolalar'},
        ),
    ]
