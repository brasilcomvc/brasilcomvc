from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

import mistune


register = template.Library()


@register.filter('markdown', is_safe=True)
@stringfilter
def to_markdown(text):
    return mark_safe(mistune.markdown(text))
