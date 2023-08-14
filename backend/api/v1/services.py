from django.contrib.contenttypes.models import ContentType
from news.models import Like


def likes_getting(obj, user):
    obj_type = ContentType.objects.get_for_model(obj)
    return Like.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user)


def add_like(obj, user):
    """Лайкает `obj`.
    """
    obj_type = ContentType.objects.get_for_model(obj)
    like, is_created = Like.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user)
    return is_created


def remove_like(obj, user):
    """Удаляет лайк с `obj`.
    """
    presence = False
    like = likes_getting(obj, user)
    if like:
        presence = True
        like.delete()
    return presence


def is_fan(obj, user) -> bool:
    """Проверяет, лайкнул ли `user` `obj`.
    """
    if not user.is_authenticated:
        return False
    like = likes_getting(obj, user)
    return like.exists()
