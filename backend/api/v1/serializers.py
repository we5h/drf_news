from rest_framework import serializers
from news.models import News, Comment
from . import services


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
    comments = CommentSerializer(many=True, read_only=True, source='less_comments')
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id',
                  'title',
                  'text',
                  'author',
                  'is_fan',
                  'comments_amount',
                  'likes_amount',
                  'comments']
        read_only_fields = ['date', 'likes_amount', 'comments_amount']

    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` `obj`)."""
        user = self.context.get('request').user
        return services.is_fan(obj, user)
