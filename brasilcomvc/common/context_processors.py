from django.conf import settings


def social_auth_facebook_key(request):
    return {'SOCIAL_AUTH_FACEBOOK_KEY': settings.SOCIAL_AUTH_FACEBOOK_KEY}
