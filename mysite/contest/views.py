from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from django.template import loader
from .models import *
# Create your views here.

def index(request):
    post = PicturePost.objects.all()
    return render(request, 'index.html', {'post': post})

def user_profile(request):
    template = loader.get_template('user_profile.html')
    return HttpResponse(template.render())

def photo(request):
    template = loader.get_template('photo.html')
    return HttpResponse(template.render())