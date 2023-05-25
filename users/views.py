from urllib.request import urlopen
from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .detection import *
from .forms import LoginForm, RegisterForm
from .models import *
from django.contrib.auth.models import User

# Create your views here.


def password_check(password, pass_confirm):
    error = list()
    if password != pass_confirm:
        error.append(' Both passwords are not equal')
    elif len(password) < 8:
        error.append(' The password length must be atleast 8 characters')
    elif password == '12345678' or password == 'abcdefgh':
        error.append(' The password is too common')
    else:
        return 'No error'
    return error


def clean_email(email):
    # email = email.cleaned_data['email']
    if User.objects.filter(email=email).exists():
        # raise ValidationError("Email already exists")
        return 'Error'
    return email


def clean_username(username):
    if User.objects.filter(username=username).exists():
        # raise ValidationError("Email already exists")
        return 'Error'
    return username




def signin(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/signin.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=email, password=password)

            if user is not None:
                profile = Profile.objects.get(email=email)
                face = Face.objects.get(profile=profile)
                #if face_login(str(profile.profile_image)):
                if face_login(str(face.face)):
                    login(request, user)
                    return redirect('home1')
                return render(request, 'users/signin.html', {'errors': 'Unauthorised access! Please bring your face '
                                                                       'close to the webcam'})

                # return render(request, 'index.html', {'user': user})

            return render(request, 'users/signin.html', {'errors': 'Username or password is incorrect!'})


# return render(request, 'users/signup.html')



def signup(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/signup.html', {'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(request)

        if form.is_valid():

            first_name = request.POST['f_name']
            last_name = request.POST['l_name']
            phone = request.POST['phone']
            email = request.POST['email']
            password = request.POST['password1']
            pass_confirm = request.POST['password2']
            username = (first_name + last_name).lower()
            error = password_check(password, pass_confirm)
            if error != 'No error':
                return render(request, 'users/signup.html', {'errors': error})
            error = clean_email(email)
            if error == 'Error':
                return render(request, 'users/signup.html', {'errors_email': 'Email already exists!'})
            error = clean_username(username)
            if error == 'Error':
                return render(request, 'users/signup.html', {'errors_username': 'Username already exists!'})
            user = User.objects.create_user(email=email, password=password, username=username)
            user.save()
            profile = Profile(first_name=first_name, last_name=last_name, phone=phone,
                              username=user.username, email=email)  # create new model instance
            profile.save()

            messages.success(request, 'You have signed up successfully.')
            login(request, user)
            return redirect('reg_face')
        else:
            return render(request, 'users/signup.html', {'form': form})


@login_required(login_url='/signin')
def signout(request):
    logout(request)
    #return render(request, 'users/signin.html')
    return redirect('signin')


@login_required(login_url='/signin')
def reg_face(request):
    errorCheck = request.session.get('errorCheck')
    if errorCheck:
        return render(request, 'users/reg_face.html', {'error': 'Please capture a proper image of yourself to register.'})
    return render(request, 'users/reg_face.html', {'error': None})

@login_required(login_url='/signin')
def register_captured_face(request):
    path = request.POST["src"]
    profile = Profile.objects.get(email=request.user.email)
    image = NamedTemporaryFile()
    image.write(urlopen(path).read())
    image.flush()
    image = File(image)
    name = str(profile.username)
    name += '.jpg'
    image.name = name
    if image is not None:
        face = Face.objects.create(profile=profile, face=image)
        face.save()
        _mutable = request.GET._mutable
        request.GET._mutable = True
        if check_face_errors(str(face.face)):
            return redirect('home1')
        face.delete()
    request.session['errorCheck'] = True
    request.session.modified = True
    return redirect('reg_face')





