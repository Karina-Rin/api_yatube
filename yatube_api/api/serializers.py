from rest_framework import serializers

from posts.models import Comment, Group, Post, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "username"
        ref_name = "ReadOnlyUsers"


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        fields = "__all__"
        model = Post
        read_only_fields = (
            "pub_date",
            "group",
        )


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "title")


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        model = Comment
        fields = "__all__"
