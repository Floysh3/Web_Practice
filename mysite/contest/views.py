from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework import generics, permissions
from rest_framework import serializers
from .permissions import IsOwnerOrReadOnly
from .utils import *
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

menu = [{'title': 'Опубликовать фотографию', 'url_name': 'pub_photo'}, ]

class Index(DataMixin, ListView, LoginRequiredMixin):
    model = PicturePost
    template_name = 'base.html'
    context_object_name = 'post'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        kwargs['form'] = AddPostForm

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return PicturePost.objects.filter(is_published=True)

class MyUserList(generics.ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = serializers.MyUserSerializer


class PhotoList(generics.ListCreateAPIView):
    queryset = PicturePost.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PicturePost.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                              IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


def user_profile(request, user_id):
    post = PicturePost.objects.all()
    list_of_users = MyUser.objects.all()
    context = {'menu': menu,
               'title': 'Страница пользователя',
               'list_of_users': list_of_users,
               'user_id': user_id,
               'post': post,
               }
    return render(request, 'user_profile.html', context=context)


def list_of_users(request):
    list_of_users = MyUser.objects.all()
    return render(request, 'list_of_users.html',
                  {'menu': menu, 'list_of_users': list_of_users, 'title': 'Список всех пользователей'})



class Pub_Photo(LoginRequiredMixin, CreateView, AddPostForm):
    form_class = AddPostForm
    login_url = reverse_lazy('login')
    template_name = 'pub_photo.html'
    model = PicturePost
    success_url = reverse_lazy('pub_photo')

    def get_context_data(self, **kwargs):
        kwargs['form'] = AddPostForm
        kwargs['menu'] = menu
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

def about(request):
        return HttpResponse('Информация о сайте')

def contact(request):
        return HttpResponse('Служба поддержки')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')

        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')

        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


def show_photo(request, photo_id):
    post = get_object_or_404(PicturePost, pk=photo_id)
    context = {'menu': menu,
               'title': 'Страница фотографии',
               'post': post,
               }

    return render(request, 'pub_photo.html', context=context)

def top_photos(request):
    return HttpResponse('Топ фотографий')



def logout_user(request):
    logout(request)

    return redirect('index')