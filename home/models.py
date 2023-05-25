import uuid

from django.db import models
from django import forms
from datetime import datetime
from users import models as m


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=255)
    posted_date = models.DateTimeField(default=datetime.now)
    # image = models.ImageField(upload_to='post_images')
    description = models.TextField(max_length=5000)
    no_of_likes = models.IntegerField(default=0)
    no_of_comments = models.IntegerField(default=0)

class LikePost(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='post_images')


class PostComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=255)
    posted_date = models.DateTimeField(default=datetime.now)
    # image = models.ImageField(upload_to='post_images')
    description = models.TextField(max_length=5000, null=True)
    no_of_likes = models.IntegerField(default=0)
    commenting_post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)


class CommentImage(models.Model):
    post = models.ForeignKey(PostComment, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='comment_images')


class LikePostComment(models.Model):
    post = models.ForeignKey(PostComment, on_delete=models.CASCADE, default=None)
    user = models.CharField(max_length=255)

class Bookmark(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    user = models.CharField(max_length=255)
