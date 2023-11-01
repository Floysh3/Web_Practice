from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .serializers import PostSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


from .forms import CustomUserCreationForm
# Create your views here.

menu = [{'title':"Войти", 'url_name':'login'},{'title':"Регистрация", 'url_name':'signup'}]

def index(request):
    posts = PicturePost.objects.all()
    return render(request, 'home.html', {'menu': menu, 'posts':posts, 'title':'Главная страница'})

def user_profile(request):
    template = loader.get_template('user_profile.html')
    return render(request, 'user_profile.html', {'menu': menu, 'title':'Страница пользователя'})

def photo(request):
    template = loader.get_template('photo.html')
    return HttpResponse(template.render())


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class GetPostInfoView(APIView):
    def get(self, request):
        queryset = PicturePost.objects.all()
        serializer_for_queryset = PostSerializer(instance=queryset, many=True)
        return Response(serializer_for_queryset.data)
