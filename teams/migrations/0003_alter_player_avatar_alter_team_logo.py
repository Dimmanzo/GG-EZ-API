# Generated by Django 5.1.3 on 2024-12-02 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='image'),
        ),
    ]