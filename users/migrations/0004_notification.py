# Generated by Django 3.2.11 on 2023-05-24 05:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_face'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=2084)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('is_seen', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]