# Generated by Django 3.2.11 on 2023-05-24 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notify_from_user',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
