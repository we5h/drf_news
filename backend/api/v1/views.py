import datetime

from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .authentication import CustomAuthentication
from .permissions import IsAuthorAdminOrReadOnly, IsAuthorPostOwnerAdminOrReadOnly
from .mixins import ListPostDeleteViewSet, LikedMixin

from backend.settings import TOKEN_EXPIRE_TIME
from news.models import Token, User, News

from .serializers import TokenObtainSerializer, NewsSerializer, CommentSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def obtain_token_view(request):
    """Запрос на получение токена."""

    serializer = TokenObtainSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = get_object_or_404(User, username=username)
    if user.check_password(password):
        utc_now = datetime.datetime.utcnow()

        Token.objects.filter(
            user=user,
            date__lt=utc_now - TOKEN_EXPIRE_TIME).delete()

        token, created = Token.objects.get_or_create(
            user=user,
            defaults={
                'key': get_random_string(length=40)
            })
        return Response({
            'token': token.key
        })
    raise AuthenticationFailed(detail='Invalid password.')


class NewsViewSet(LikedMixin,
                  viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthorAdminOrReadOnly]
    authentication_classes = [CustomAuthentication]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def destroy(self, *args, **kwargs):
        super().destroy(*args, **kwargs)
        return Response({
            "detail": "Post has been deleted successfully."
            },
            status=status.HTTP_200_OK
        )


class CommentViewSet(ListPostDeleteViewSet):
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthorPostOwnerAdminOrReadOnly]
    authentication_classes = [CustomAuthentication]

    def get_queryset(self):
        news = get_object_or_404(News, id=self.kwargs.get("news_id"))
        return news.comments.all()

    def perform_create(self, serializer):
        news = get_object_or_404(News, id=self.kwargs.get("news_id"))
        serializer.save(
            post=news,
            author=self.request.user)

    def destroy(self, *args, **kwargs):
        super().destroy(*args, **kwargs)
        return Response({
            "detail": "Comment has been deleted successfully."
            },
            status=status.HTTP_200_OK
        )
