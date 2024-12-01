# Generated by Django 5.1.3 on 2024-11-30 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='album_covers/'),
        ),
        migrations.AddField(
            model_name='album',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]