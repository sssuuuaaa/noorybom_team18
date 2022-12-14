# Generated by Django 4.0.6 on 2022-08-26 09:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0031_alter_feed_create_time_remove_participateitems_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 26, 18, 7, 25, 502151)),
        ),
        migrations.RemoveField(
            model_name='participateitems',
            name='user',
        ),
        migrations.AddField(
            model_name='participateitems',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='participateitems',
            name='volunteerItem',
        ),
        migrations.AddField(
            model_name='participateitems',
            name='volunteerItem',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='content.volunteeritem'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='volunteeritem',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 26, 18, 7, 25, 502151)),
        ),
    ]
