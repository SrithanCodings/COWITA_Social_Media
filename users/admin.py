from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class FollowerAdmin(admin.StackedInline):
    model = Follower
    extra = 0
    list_display = ('following', )


class FaceAdmin(admin.StackedInline):
    model = Face
    extra = 0
    list_display = ('post', 'face')


class NotificationAdmin(admin.StackedInline):
    model = Notification
    extra = 0
    list_display = ('message', 'is_seen', 'date')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone')
    inlines = [FaceAdmin, FollowerAdmin, NotificationAdmin]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Follower)
admin.site.register(Face)
admin.site.register(Notification)