# Generated by Django 3.2.11 on 2023-05-12 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230509_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face', models.ImageField(default='None', upload_to='registered faces')),
                ('profile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]