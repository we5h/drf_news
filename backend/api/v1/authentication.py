import datetime
import pytz
from rest_framework import authentication, exceptions

from backend.settings import TOKEN_EXPIRE_TIME
from news.models import Token


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        raw_token = request.META.get('HTTP_AUTHORIZATION')
        if not raw_token:
            return None

        token_key = raw_token.replace('Token ', '')

        try:
            user_token = Token.objects.select_related('user').get(key=token_key)
            user = user_token.user
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed(
                'Invalid token'
            )

        utc = pytz.UTC
        utc_now = datetime.datetime.utcnow().replace(tzinfo=utc)

        if user_token.date.replace(tzinfo=utc) < utc_now - TOKEN_EXPIRE_TIME:
            raise exceptions.AuthenticationFailed(
                'Token has expired'
            )
        return (user, None)
