from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from users.models import *

# from . import urls
from django.shortcuts import HttpResponseRedirect, HttpResponse
# from .models import Products


# creates a Tk() object


@login_required(login_url='user/signin')
def index(request):  #Home
    profile = Profile.objects.get(email=request.user.email)
    followers = Follower.objects.filter(following=request.user.email)
    followers_list = list()
    for follower in followers:
        followers_list.append(follower)
    you_as_follower = Follower.objects.create(follower=profile, following=profile.email)
    followers_list.append(you_as_follower)
    followers = followers_list.copy()
    posts = list()
    for follower in followers:
        posts.append(Post.objects.filter(user=follower.follower.email))
    posts_list = list()
    for post in posts:
        if len(post)>1:
            for post1 in post:
                posts_list.append(post1)
        else:
            posts_list.append(post)
    posts = reversed(posts_list)
    post.order_by('posted_date')
    images = PostImage.objects.all()
    # print(request.user.email)
    all_profiles = Profile.objects.all()
    comments = PostComment.objects.all()
    you_as_follower.delete()
    return render(request, 'index.html', {
        'posts': posts,
        'images': images,
        'profile': profile,
        'all_profiles': all_profiles,
        'comments': comments,
        # 'stories': stories,
        # 'user': user
    })



def notifications(request):
    all_profiles = Profile.objects.all()
    profile = Profile.objects.get(email=request.user.email)
    notifications = Notification.objects.filter(profile=profile)
    for notification in notifications:
        notification.is_seen = True
        notification.save()
    profile.no_of_notifications = 0
    profile.save()
    notifications = reversed(notifications)
    return render(request, 'notifications.html', {
        'notifications': notifications,
        'all_profiles': all_profiles,
    })


@login_required(login_url='/user/signin')
def settings(request):
    profile = Profile.objects.get(username = request.user.username)
    print(request.user.email)
    print(profile.dob)
    dob = str(profile.dob)
    return render(request, 'settings.html', {
        'profile': profile,
        'dob': dob
    })



@login_required(login_url='user/signin')
def bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user.email)
    posts = list()
    for bookmark in bookmarks:
        print(bookmark.post.id)
        posts.append(Post.objects.filter(id=bookmark.post.id))
    print(posts)
    all_profiles = Profile.objects.all()
    likes = LikePost.objects.all()
    return render(request, 'bookmarks.html', {
        'posts': posts,
        'all_profiles': all_profiles,
        'likes': likes,
    })


@login_required(login_url='user/signin')
def profile(request):
    email = request.GET['email']
    follow = True
    if request.user.email == email:
        follow = False
    profile = Profile.objects.get(email = email)
    posts = Post.objects.filter(user = email)
    images = PostImage.objects.all()
    followings = Follower.objects.filter(follower=profile)
    followings_profile = list()
    for following in followings:
        following_profile = Profile.objects.get(email = following.following)
        followings_profile.append(following_profile)
    followings = followings_profile.copy()
    followers = Follower.objects.filter(following=email)
    # all_followers = Follower.objects.all()
    # for follower in all_followers:
    #     if follower.follower.email == email:
    return render(request, 'profile.html', {
        'email': email,
        'profile': profile,
        'posts': posts,
        'images': images,
        'followings': followings,
        'followers': followers,
        'follow': follow
    })


def index_login(request):
    return HttpResponseRedirect(reverse("home"))


@login_required(login_url='user/signin')
def show_comments(request):
    post_id = request.GET['post_id']
    post = Post.objects.get(id=post_id)
    comments = PostComment.objects.filter(commenting_post= post)
    images = PostImage.objects.filter(post=post)
    all_profile = Profile.objects.all()
    profile = Profile.objects.get(email = request.user.email)
    comment_images = []
    for comment in comments:
        image = CommentImage.objects.filter(post = comment)
        comment_images.append(image)

    comments = reversed(comments)
    # comment_likes = LikePostComment.objects.filter(post = )
    return render(request, 'comments.html', {
        'post': post,
        'comments': comments,
        'images': images,
        'all_profiles': all_profile,
        'profile': profile,
        'comment_images': comment_images
    })



@login_required(login_url='user/signin')
def instacall(request):
    profile = Profile.objects.get(email=request.user.email)
    username = profile.first_name + " " + profile.last_name
    return render(request, 'video_call.html', {
        'username': username,
    })


@login_required(login_url='user/signin')
def search(request):
    search_username = request.GET['search']
    profiles = Profile.objects.filter(username__contains=search_username)

    return render(request, 'search.html', {
        'username': search_username,
        'profiles': profiles,
    })


def about(request):
    return render(request, 'about.html')

def explore(request):
    profile = Profile.objects.get(email=request.user.email)
    posts = Post.objects.all()
    posts = reversed(posts)
    images = PostImage.objects.all()
    # print(request.user.email)
    all_profiles = Profile.objects.all()
    comments = PostComment.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
        'images': images,
        'profile': profile,
        'all_profiles': all_profiles,
        'comments': comments,
        # 'stories': stories,
        # 'user': user
    })
