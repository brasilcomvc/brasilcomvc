from django import template


register = template.Library()


@register.inclusion_tag('widgets/form_full.html')
def form_full(form, csrf_token=True):
    '''
    Shortcut to render all the form fields
    '''
    return {
        'csrf_token': csrf_token,
        'form': form,
    }


@register.inclusion_tag('widgets/form_field.html')
def form_field(field):
    '''
    Render a single field
    '''
    form = field.form

    # Prepare field HTML classes
    classes = tuple(filter(None, [
        'required' if field.field.required else None,
        'error' if field.errors else None,
    ]))

    return {
        'classes': classes,
        'field': field,
        'form_id': form.prefix or type(form).__name__.lower(),
    }


@register.inclusion_tag('widgets/form_fieldset.html')
def form_fieldset(form, legend=None, fields=None):
    '''
    Render a <fieldset> from `form` with provided space-separated fields
    '''
    return {
        'fields': list(map(lambda field: form[field], fields.split())),
        'legend': legend,
    }
