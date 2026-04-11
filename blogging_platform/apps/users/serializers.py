from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "bio", "avatar", "website")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "username", "email", "bio", "avatar", "website", "post_count", "date_joined")
        read_only_fields = ("id", "date_joined")

    def get_post_count(self, obj):
        return obj.posts.count()