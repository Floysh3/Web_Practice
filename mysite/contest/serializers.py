


from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = PicturePost
        fields = ['id', 'title', 'description', 'photo', 'author']


class MyUserSerializer(serializers.ModelSerializer):
    photos_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = MyUser
        fields = ['id', 'username', 'photos_set']

