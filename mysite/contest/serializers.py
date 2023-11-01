from rest_framework import serializers, renderers

class PostSerializer(serializers.Serializer):
    pub_date = serializers.DateTimeField(read_only=True)
    description = serializers.CharField(max_length=300)
    name = serializers.CharField(max_length=50)
    user = serializers.CharField(source='MyUser.username', max_length=150)

