from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_template_email(subject, to, template_name, context=None):
    '''
    Render a template into an email body and send it through Django's send_mail

    - The `to` parameter must be a single email address.
    - This function omits `from_email` because it expects it to exist from an
    environment variable.
    - Other parameters are omitted as well because there are no
    use for them in the current use case.
    '''
    body = render_to_string(template_name, context or {}, Context({
        'mailing_address': settings.MAILING_ADDRESS,
        'site_url': settings.BASE_URL,
        'sns_facebook': settings.SNS_FACEBOOK,
        'sns_googleplus': settings.SNS_GOOGLEPLUS,
        'sns_twitter': settings.SNS_TWITTER,
        'subject': subject,
    }))
    plain_body = strip_tags(body)

    email = EmailMultiAlternatives(
        subject=subject,
        body=plain_body,
        to=(to,))
    email.attach_alternative(body, 'text/html')
    email.send()
