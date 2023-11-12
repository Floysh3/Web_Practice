from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.http import HttpResponseNotFound

from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import LikeSerializer
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

class LikeView(CreateAPIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        post = PicturePost.objects.get(id=kwargs["id"])
        user = request.user
        like = Like.objects.create(post=post, user=user)
        return Response(LikeSerializer(like).data, status=status.HTTP_200_OK)


class UnlikeView(CreateAPIView):

    permission_classes = [IsAuthenticated, ]

    def delete(self, request, *args, **kwargs):
        user = request.user
        post = PicturePost.objects.get(kwargs=["id"])
        like = Like.objects.get(user=user, post=post)
        like.delete()
        return Response(status=status.HTTP_200_OK)