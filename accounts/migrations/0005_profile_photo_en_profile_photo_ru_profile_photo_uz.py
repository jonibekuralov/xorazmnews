# Generated by Django 5.0.3 on 2024-04-04 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo_en',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='photo_ru',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='photo_uz',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
    ]