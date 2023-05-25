# Generated by Django 3.2.11 on 2023-05-08 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('first_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=255, null=True, unique=True)),
                ('bio', models.TextField(max_length=2083, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('district', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('locality', models.CharField(max_length=255, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('dob', models.DateField(null=True)),
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('profile_image', models.ImageField(default='media/profile_image/default_profile.jpg', upload_to='profile_image')),
                ('background_image', models.ImageField(default='media/background_image/default_background.jpg', upload_to='background_image')),
                ('no_of_followers', models.IntegerField(default=0)),
            ],
        ),
    ]