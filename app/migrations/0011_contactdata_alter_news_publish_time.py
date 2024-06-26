# Generated by Django 4.2.10 on 2024-02-27 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_news_publish_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 27, 12, 55, 25, 892075, tzinfo=datetime.timezone.utc)),
        ),
    ]
