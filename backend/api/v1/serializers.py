from rest_framework import serializers
from news.models import News, Comment


class TokenObtainSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author']
        read_only_fields = ['date']


class NewsSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'text', 'author', 'comments', 'likes_amount']
        read_only_fields = ['date', 'likes_amount']
