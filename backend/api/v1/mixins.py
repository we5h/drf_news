from rest_framework import mixins, generics


class MyUpdateDestroyAPIView(
    generics.GenericAPIView,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    pass