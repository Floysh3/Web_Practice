from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyUser(User):
    email_address = models.EmailField(max_length=50)
    registration_date = models.DateField(auto_now=True)
    likes = models.ForeignKey("Like", on_delete=models.CASCADE, null=True)
    comments = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True)

class PicturePost(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    likes = models.ForeignKey("Like", on_delete=models.CASCADE, null=True)
    comments = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=300)
    name = models.CharField(max_length=50)
    likes_quantity = models.IntegerField()
    comments_quantity = models.IntegerField()


class Comment(models.Model):
    pub_date = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=300)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(PicturePost, on_delete=models.CASCADE, null=True)


class Like(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(PicturePost, on_delete=models.CASCADE, null=True)



