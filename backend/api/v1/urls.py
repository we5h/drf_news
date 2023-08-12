from django.urls import include, path

from .views import obtain_token_view

urlpatterns = [
    path('auth/', obtain_token_view, name='token_obtain'),
    # path('', include(router.urls)),
]