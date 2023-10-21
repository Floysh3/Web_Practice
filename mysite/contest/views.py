from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.http import HttpResponseNotFound
# Create your views here.

def index(request):
    posts = PicturePost.objects.all()
    return render(request, 'index.html', {'posts': posts, 'title':'Главная страница'})

def user_profile(request):
    template = loader.get_template('user_profile.html')
    return HttpResponse(template.render())

def photo(request):
    template = loader.get_template('photo.html')
    return HttpResponse(template.render())