# Generated by Django 4.1 on 2022-08-27 00:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0034_alter_feed_create_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 9, 47, 2, 321083)),
        ),
        migrations.AlterField(
            model_name='volunteeritem',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 9, 47, 2, 322077)),
        ),
    ]