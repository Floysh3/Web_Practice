from django.contrib import admin
from .models import PicturePost
from .models import MyUser, Like, Comment
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin



admin.site.register(PicturePost)
admin.site.register(MyUser)
admin.site.register(Like)
admin.site.register(Comment)

