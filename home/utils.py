from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from users.models import *

# from . import urls
from django.shortcuts import HttpResponseRedirect, HttpResponse
# from .models import Products


@login_required(login_url='user/signin')
def upload(request):

    if request.method == 'POST':
        user = request.user.email
        images = request.FILES.getlist('file_input')
        description = request.POST['description']

        new_post = Post.objects.create(user=user, description=description)
        new_post.save()
        print(images)
        for image in images:
            new_image = PostImage.objects.create(post=new_post, images=image)
            new_image.save()

        profile = Profile.objects.get(email=user)
        followers = Follower.objects.filter(following=user)
        for follower in followers:
            add_notification(f'{profile.first_name} {profile.last_name} has uploaded a new post', follower.follower, user)

        return redirect('home')
    return redirect('home')


@login_required(login_url='user/signin')
def settingsSave(request):
    profile = Profile.objects.get(username = request.user.username)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        locality = request.POST['locality']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        bio = request.POST['bio']
        dob = request.POST['dob']
        profile_img = request.FILES.get('profile')
        background_img = request.FILES.get('background')

        profile.first_name = first_name
        profile.last_name = last_name
        profile.email = email
        profile.locality = locality
        profile.city = city
        profile.state = state
        profile.country = country
        profile.bio = bio
        print(dob)
        print(profile_img)
        if dob != "":
            print('dob')
            profile.dob = dob
        if profile_img != None:
            profile.profile_image = profile_img
        if background_img != None:
            profile.background_image = background_img

        profile.save()
        return redirect('home')


@login_required(login_url='user/signin')
def deletePost(request, post_id=None):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    response = redirect('profile')
    response['Location'] += '?email=' + str(request.user.email)
    return response


@login_required(login_url='user/signin')
def likePost(request, post_id):
    email = request.user.email
    post = Post.objects.get(id=post_id)
    no_of_likes = post.no_of_likes
    is_liked = False
    liking_people = LikePost.objects.filter(post=post)
    print(liking_people)
    for liking_person in liking_people:
        if liking_person.user != email:
            continue
        is_liked = True
    if is_liked:
        liking_person = liking_people.filter(user=email)
        liking_person.delete()
        no_of_likes -= 1
    else:
        no_of_likes += 1
        liking_person = LikePost.objects.create(user=email, post=post)
        liking_person.save()
    post.no_of_likes = no_of_likes
    post.save()
    like_redirect = request.GET['likeRedirect']
    if like_redirect == 'index':
        return redirect("home")
    elif like_redirect == 'comments':
        return redirect(('{}?post_id=' + post_id).format(reverse('comment')))


@login_required(login_url='user/signin')
def commentPost(request, post_id):

    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        user = request.user.email
        comment = request.POST['comment']
        images = request.FILES.getlist('comment_img')

        new_post = PostComment.objects.create(user=user, description=comment, commenting_post=post)
        new_post.save()
        print(images)
        for image in images:
            new_image = CommentImage.objects.create(post=new_post, images=image)
            new_image.save()
        post.no_of_comments += 1
        post.save()
        return redirect(('{}?post_id=' + post_id).format(reverse('comment')))
    return redirect('comment')


@login_required(login_url='user/signin')
def like_comment(request, comment_id):
    email = request.user.email
    comment = PostComment.objects.get(id=comment_id)
    no_of_likes = comment.no_of_likes
    is_liked = False
    liking_people = LikePostComment.objects.filter(post=comment)
    print(liking_people)
    for liking_person in liking_people:
        if liking_person.user != email:
            continue
        is_liked = True
    if is_liked:
        liking_person = liking_people.filter(user=email)
        liking_person.delete()
        no_of_likes -= 1
    else:
        no_of_likes += 1
        liking_person = LikePostComment.objects.create(user=email, post=comment)
        liking_person.save()
    comment.no_of_likes = no_of_likes
    comment.save()
    post = comment.commenting_post
    post_id = str(post.id)
    return redirect(('{}?post_id=' + post_id).format(reverse('comment')))


@login_required(login_url='user/signin')
def bookmark_post(request):
    post_id = request.GET['post']
    post = Post.objects.get(id=post_id)
    posts_bookmarked = Bookmark.objects.filter(user=request.user.email)
    is_bookmarked = False
    for post_bookmarked in posts_bookmarked:
        if post.id == post_bookmarked.post.id:
            #post_bookmarked.delete()
            is_bookmarked = True
            break
    if not is_bookmarked:
        bookmark = Bookmark.objects.create(post=post, user=request.user.email)
        bookmark.save()
    else:
        bookmark = Bookmark.objects.filter(post=post)
        bookmark.delete()
    return redirect('home')


def add_notification(message, user, notify_from_user):
    notification = Notification.objects.create(profile=user, message=message, notify_from_user=notify_from_user)
    notification.save()
    profile = Profile.objects.get(email=notify_from_user)
    profile.no_of_notifications += 1
    user.save()


@login_required(login_url='user/signin')
def follow_user(request):
    email = request.GET['email_id']
    user_email = request.user.email
    follower_profile = Profile.objects.get(email=email)
    following_profile = Profile.objects.get(email=user_email)
    all_followers = Follower.objects.all()
    for follower in all_followers:
        try:
            old_follower_model = Follower.objects.get(follower=follower_profile, following=user_email)
            follower_profile.no_of_followers -= 1
            following_profile.no_of_following -= 1
            old_follower_model.delete()
            following_profile.save()
            follower_profile.save()
            response = redirect('profile')
            response['Location'] += '?email=' + str(email)
            return response
        except BaseException:
            follower_profile.no_of_followers += 1
            following_profile.no_of_following += 1
            new_follower_model = Follower.objects.create(follower=follower_profile, following=user_email)
            new_follower_model.save()
            following_profile.save()
            follower_profile.save()
            add_notification(f'{following_profile.first_name} {following_profile.last_name} has followed you',
                             follower_profile, user_email)
            response = redirect('profile')
            response['Location'] += '?email=' + str(email)
            return response