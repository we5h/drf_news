from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models


class BaseModel(models.Model):
    """Абстрактная модель с датой создания."""

    date = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    """Пользователи."""
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Like(models.Model):
    """Лайки."""
    user = models.ForeignKey(User,
                             related_name='likes',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class News(BaseModel):
    """Новости."""
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=256,
        unique=True,
        db_index=True
    )
    text = models.TextField(
        verbose_name='Текст',
        max_length=8500
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='news',
    )
    likes = GenericRelation(Like)

    @property
    def likes_amount(self):
        return self.likes.count()

    @property
    def comments_amount(self):
        return self.comments.count()

    class Meta:
        ordering = ['title']
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title[:25]

    def less_comments(self):
        return Comment.objects.all().filter(post=self).order_by("-id")[:10]


class Comment(BaseModel):
    """Комментарии."""
    text = models.TextField(
        verbose_name='Текст комментария',
        max_length=3500
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='comments',
    )

    post = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        verbose_name='Пост',
        related_name='comments',
    )

    class Meta:
        ordering = ['date']
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text[:25]


class Token(BaseModel):
    """Токены."""
    user = models.OneToOneField(
        User, related_name='auth_token',
        on_delete=models.CASCADE,
        verbose_name='Пользователь, которому принадлежит токен'
    )

    key = models.CharField(
        verbose_name='Токен',
        max_length=40,
        db_index=True,
        unique=True
    )

    def __str__(self):
        return f'{self.user.username} - {self.key}'

    class Meta:
        ordering = ['date']
        verbose_name = "Токен"
        verbose_name_plural = "Токены"
