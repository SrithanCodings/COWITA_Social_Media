from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path

from COWITA_Media import settings as s
from .views import *
from .utils import *

urlpatterns = [
    path('', index, name='home'),
    path('explore', explore, name='explore'),
    path('comment', show_comments, name='comment'),
    path('notifications', notifications, name='notifications'),
    path('bookmarks', bookmarks, name='bookmarks'),
    path('profile', profile, name='profile'),
    path('upload', upload, name='upload'),
    path('settings', login_required(settings, login_url='users/signin'), name='settings'),
    path('settingsSave', settingsSave, name='settingsSave'),
    path('deletePost/<post_id>', deletePost, name='deletePost'),
    path('likePost/<post_id>', likePost, name='likePost'),
    path('commentPost/<post_id>', commentPost, name='commentPost'),
    path('like_comment/<comment_id>', like_comment, name='like_comment'),
    path('bookmarkPost', bookmark_post, name='bookmarkPost'),
    path('follow', follow_user, name='followUser'),
    path('videocall', instacall, name='instacall'),
    path('search', search, name='search'),
    path('about', about, name='about')

    ] + static(s.MEDIA_URL, document_root= s.MEDIA_ROOT)