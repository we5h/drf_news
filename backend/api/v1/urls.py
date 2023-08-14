from django.urls import include, path

from .views import obtain_token_view, NewsViewSet, CommentViewSet
from rest_framework import routers

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
