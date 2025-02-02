# Generated by Django 3.2.4 on 2024-12-14 08:35

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='avatar',
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
