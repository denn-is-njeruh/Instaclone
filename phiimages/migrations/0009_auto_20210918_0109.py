# Generated by Django 3.2.7 on 2021-09-17 22:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('phiimages', '0008_remove_image_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['posted_on']},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['posted_on']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='body',
        ),
        migrations.RemoveField(
            model_name='image',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='image',
            name='time_created',
        ),
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='image',
            name='posted_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='phiimages.image'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='posted_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
