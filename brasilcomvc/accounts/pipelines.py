def set_user_info_from_auth_provider(backend, user, details, *args, **kwargs):
    """Social auth pipeline to set user info returned from auth provider
    """
    if not user:
        return

    user.email = details['email']
    user.full_name = details['fullname']

    backend.strategy.storage.user.changed(user)
