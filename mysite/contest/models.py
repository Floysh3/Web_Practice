from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse



# Create your models here.
class MyUser(AbstractUser):
    def get_absolute_url(self):
        return reverse('user_profile', kwargs={'user_id': self.pk})

    class Meta:
        db_table = 'MyUser_app_db'

class Like(models.Model):
    author = models.ForeignKey('MyUser', on_delete=models.CASCADE)
    photo = models.ForeignKey('PicturePost', on_delete=models.CASCADE)
    like_published = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        db_table = 'Like_app_db'

class PicturePost(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.CharField(max_length=255, verbose_name='Описание')
    author = models.ForeignKey('MyUser', related_name='post', on_delete=models.CASCADE, verbose_name='Автор')
    photo_published = models.DateTimeField(auto_now_add=True)
    photo_change = models.DateTimeField(auto_now=True)
    quantity_comments = models.IntegerField(default=0)
    quantity_likes = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    likes = GenericRelation(Like)

    class Meta:
        db_table = 'Photo_app_db'

    def get_absolute_url(self):
        return reverse('photo', kwargs={'photo_id': self.pk})



class Comment(models.Model):
    author = models.ForeignKey('MyUser', on_delete=models.CASCADE)
    photo = models.ForeignKey('PicturePost', on_delete=models.CASCADE)
    comment_published = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        db_table = 'Comment_app_db'





