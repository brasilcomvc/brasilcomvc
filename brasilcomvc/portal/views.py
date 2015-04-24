from django.conf import settings
from django.http import Http404, HttpResponsePermanentRedirect


def blog_redirect(request):
    """Simple redirect to blog URL.
    """
    if settings.BLOG_URL == '':
        raise Http404()
    return HttpResponsePermanentRedirect(settings.BLOG_URL)

