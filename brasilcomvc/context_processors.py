from django.conf import settings


def sns_links(request):
    return {
        'sns_facebook': settings.SNS_FACEBOOK,
        'sns_googleplus': settings.SNS_GOOGLEPLUS,
        'sns_twitter': settings.SNS_TWITTER,
    }
