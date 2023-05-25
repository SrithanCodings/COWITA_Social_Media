from django.conf.urls.static import static
from .views import *
from home import views as v
from django.urls import path
from django.shortcuts import render, redirect
from home import views as v
from COWITA_Media import settings


urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('signup/', signup, name='signup'),
    path('reg_face/', reg_face, name='reg_face'),
    path('reg_face/register_captured_face', register_captured_face, name='register_captured_face'),
    path('', v.index_login, name='home1'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
