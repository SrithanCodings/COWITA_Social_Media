from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True, unique=True)
    bio = models.TextField(max_length=2083, null=True)
    country = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    district = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    locality = models.CharField(max_length=255, null=True)
    phone = models.IntegerField(null=True)
    dob = models.DateField(null=True)
    username = models.CharField(max_length=255, primary_key=True)
    profile_image = models.ImageField(upload_to='profile_image', default='media/profile_image/default_profile.jpg')
    background_image = models.ImageField(upload_to='background_image',default= 'media/background_image/default_background.jpg')
    no_of_followers = models.IntegerField(default=0)
    no_of_following = models.IntegerField(default=0)
    no_of_notifications = models.IntegerField(default=0)
    # id = models.CharField(max_length=255, default=username)

class Follower(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    following = models.CharField(max_length=255)

class Face(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    face = models.ImageField(upload_to='registered faces', default='None')


class Notification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    notify_from_user = models.CharField(max_length=255, default=None, null=True)
    message = models.TextField(max_length=2084)
    date = models.DateTimeField(default=datetime.now)
    is_seen = models.BooleanField(default=False)
