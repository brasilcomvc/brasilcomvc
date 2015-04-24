from django.conf import settings


def api_keys(request):
    return {
        'GOOGLE_API_KEY': settings.GOOGLE_API_KEY,
        'GOOGLE_ANALYTICS_ID': settings.GOOGLE_ANALYTICS_ID,
        'FACEBOOK_API_KEY': settings.FACEBOOK_API_KEY,
    }


def blog_url(request):
    return {'BLOG_URL': settings.BLOG_URL}
