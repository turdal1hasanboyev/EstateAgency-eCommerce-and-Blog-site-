# Generated by Django 5.1.2 on 2024-11-04 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Mol-mulk', 'verbose_name_plural': 'Mollar/Mulklar'},
        ),
        migrations.AddField(
            model_name='property',
            name='amenities',
            field=models.ManyToManyField(blank=True, to='eCommerce.amenities'),
        ),
    ]