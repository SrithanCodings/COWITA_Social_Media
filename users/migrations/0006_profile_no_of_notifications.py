# Generated by Django 3.2.11 on 2023-05-24 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_notification_notify_from_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='no_of_notifications',
            field=models.IntegerField(default=0),
        ),
    ]
