# Generated by Django 4.1 on 2022-08-27 02:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "content",
            "0032_alter_feed_create_time_remove_participateitems_user_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="feed",
            name="create_time",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 27, 11, 51, 47, 249597)
            ),
        ),
        migrations.AlterField(
            model_name="volunteeritem",
            name="create_time",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 27, 11, 51, 47, 250593)
            ),
        ),
    ]
