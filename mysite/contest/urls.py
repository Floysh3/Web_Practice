from django.urls import path
from . import views
from .views import SignUpView

urlpatterns=[
    path('', views.index, name='index'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('photo/', views.photo, name='photo'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('api/contest/', views.GetPostInfoView.as_view()),


]
