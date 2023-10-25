from django.contrib import admin
from .models import PicturePost
from .models import MyUser, Like, Comment
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    addd_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = MyUser
    list_display = ['email', 'username']

admin.site.register(PicturePost)
admin.site.register(MyUser, CustomUserAdmin)
admin.site.register(Like)
admin.site.register(Comment)

