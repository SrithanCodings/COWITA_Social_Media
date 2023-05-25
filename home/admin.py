from django.contrib import admin
from .models import *


# Register your models here.


class PostImageAdmin(admin.StackedInline):
    model = PostImage
    extra = 0
    list_display = ('post', 'images')


class LikePostAdmin(admin.StackedInline):
    model = LikePost
    extra = 0
    list_display = ('post', 'user')


class LikePostCommentAdmin(admin.StackedInline):
    model = LikePostComment
    extra = 0
    list_display = ('user')


class CommentImageAdmin(admin.StackedInline):
    model = CommentImage
    extra = 0
    list_display = ('post', 'images')


class CommentInline(admin.StackedInline):
    model = PostComment
    extra = 0


class PostCommentAdmin(admin.ModelAdmin):
    model = PostComment
    inlines = [CommentImageAdmin, LikePostCommentAdmin]
    # extra = 0
    list_display = ('id', 'user', 'posted_date', 'description')


class InlinePostCommentAdmin(admin.StackedInline):
    model = PostComment
    extra = 0
    list_display = ('id', 'user', 'posted_date', 'description')


class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [PostImageAdmin, LikePostAdmin, InlinePostCommentAdmin]
    list_display = ('id', 'posted_date')
    readonly_fields = ['user']
    # raw_id_fields = ['user']


admin.site.register(Post, PostAdmin)
admin.site.register(PostComment)
admin.site.register(Bookmark)
