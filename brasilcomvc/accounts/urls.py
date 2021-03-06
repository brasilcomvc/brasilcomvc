from django.conf.urls import url
from django.views.generic import RedirectView

from .views import (
    DeleteUser,
    login,
    logout,
    password_reset,
    password_reset_confirm,
    password_reset_sent,
    EditNotifications,
    EditPersonalInfo,
    EditProfessionalInfo,
    EditSecuritySettings,
    EditUserAddress,
    Signup,
)


urlpatterns = (
    # User Login
    url(r'^login/$',
        login, name='login'),

    # User Logout
    url(r'^logout/$',
        logout, name='logout'),

    # Password Reset
    url(r'^esqueci-senha/$',
        password_reset, name='password_reset'),

    # Password Reset Sent
    url(r'^esqueci-senha/enviado$',
        password_reset_sent, name='password_reset_sent'),

    # Password Reset Confirm
    url(r'^esqueci-senha/redefinir/(?P<uidb64>[^-]+)-(?P<token>[^$]+)$',
        password_reset_confirm, name='password_reset_confirm'),

    # User Signup
    url(r'^cadastro/$',
        Signup.as_view(), name='signup'),

    # Edit Dashboard
    url(r'^editar/$',
        RedirectView.as_view(pattern_name='accounts:edit_personal_info'),
        name='edit_dashboard'),

    # Edit Personal Info
    url(r'^editar/info-pessoal/$',
        EditPersonalInfo.as_view(), name='edit_personal_info'),

    # Edit Professional Info
    url(r'^editar/profissional/$',
        EditProfessionalInfo.as_view(), name='edit_professional_info'),

    # Edit Notifications
    url(r'^editar/notificacoes/$',
        EditNotifications.as_view(), name='edit_notifications'),

    # Edit Security Settings
    url(r'^editar/seguranca/$',
        EditSecuritySettings.as_view(), name='edit_security_settings'),

    # Edit User Address
    url(r'^editar/endereco/$',
        EditUserAddress.as_view(), name='edit_user_address'),

    # User Delete
    url(r'^remover-conta/$',
        DeleteUser.as_view(), name='delete_user'),
)
