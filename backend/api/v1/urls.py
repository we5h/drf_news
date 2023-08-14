from django.urls import include, path

from .views import obtain_token_view, NewsViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('auth/', obtain_token_view, name='token_obtain'),
    # path('news/', NewsListView.as_view(), name='news_list'),
    # path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail')
    # path('', include(router.urls)),
]

urlpatterns += router.urls