from rest_framework import serializers
from apps.post.models import Post


class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"