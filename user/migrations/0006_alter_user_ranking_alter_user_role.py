# Generated by Django 4.0.6 on 2022-08-05 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ranking',
            field=models.CharField(choices=[('Seed', 'Seed'), ('Sprout', 'Sprout'), ('Seedling', 'Seedling'), ('Tree', 'Tree'), ('Flower', 'Flower')], default='Seed', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('User', 'User')], default='User', max_length=10),
        ),
    ]