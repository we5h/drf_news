from rest_framework.decorators import action
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from . import services


class ListPostDeleteViewSet(GenericViewSet,
                            ListModelMixin,
                            CreateModelMixin,
                            RetrieveModelMixin,
                            DestroyModelMixin):
    pass


class LikedMixin:

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        """Лайкает `obj`.
        """
        obj = self.get_object()
        is_created = services.add_like(obj, request.user)
        if is_created:
            return Response({"detail": "Liked successfully."})
        else:
            return Response({"detail": "Already liked."})

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        """Удаляет лайк с `obj`.
        """
        obj = self.get_object()
        result = services.remove_like(obj, request.user)
        if result:
            return Response({"detail": "Unliked successfully."})
        return Response({"detail": "Your like haven't found for this post."})
