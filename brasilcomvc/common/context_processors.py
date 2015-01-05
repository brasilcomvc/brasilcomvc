from django.conf import settings


def api_keys(request):
    return {
        'google_api_key': settings.GOOGLE_API_KEY,
    }
