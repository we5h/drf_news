from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, NewsViewSet, obtain_token_view

router = routers.SimpleRouter()
router.register(r'news', NewsViewSet)
router.register(
    r'news/(?P<news_id>\d+)/comments',
    CommentViewSet,
    basename='comments_list'
)


urlpatterns = [
    path('auth/', obtain_token_view, name='token_obtain'),
    path('', include(router.urls)),
]
