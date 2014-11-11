from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):

    '''
    Bind login requirement to any view
    '''

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class AnonymousRequiredMixin(object):

    '''
    Make any view be accessible by unauthenticated users only
    '''

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super(AnonymousRequiredMixin, self).dispatch(
            request, *args, **kwargs)
