# Generated by Django 5.0 on 2024-03-12 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_single_coments_alter_news_publish_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Single_Coments',
        ),
    ]
