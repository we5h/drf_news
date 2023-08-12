from django.urls import include, path

from .views import obtain_token_view, NewsListView, NewsDetailView

urlpatterns = [
    path('auth/', obtain_token_view, name='token_obtain'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail')
    # path('', include(router.urls)),
]