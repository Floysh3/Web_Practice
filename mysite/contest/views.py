from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.http import HttpResponseNotFound
# Create your views here.

menu = [{'title':"Войти", 'url_name':'authorisation'},{'title':"Регистрация", 'url_name':'registration'}]

def index(request):
    posts = PicturePost.objects.all()
    return render(request, 'index.html', {'menu': menu, 'posts':posts, 'title':'Главная страница'})

def user_profile(request):
    template = loader.get_template('user_profile.html')
    return render(request, 'user_profile.html', {'menu': menu, 'title':'Страница пользователя'})

def photo(request):
    template = loader.get_template('photo.html')
    return HttpResponse(template.render())

def authorisation(request):
    template = loader.get_template('authorisation.html')
    return render(request, 'authorisation.html', {'menu': menu, 'title':'Страница авторизации'})

def registration(request):
    template = loader.get_template('registration.html')
    return render(request, 'registration.html', {'menu': menu, 'title':'Страница регистрации'})

