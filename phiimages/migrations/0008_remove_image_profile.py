# Generated by Django 3.2.7 on 2021-09-17 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phiimages', '0007_alter_image_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
    ]
