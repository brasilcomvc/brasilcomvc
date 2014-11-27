from django.conf.urls import url

from .views import (
    login,
    logout,
    EditDashboard,
    EditNotifications,
    EditPersonalInfo,
    EditProfessionalInfo,
    EditSecuritySettings,
    EditUserAddress,
    Profile,
    Signup,
)


urlpatterns = (
    # User Login
    url(r'^login/$',
        login, name='login'),

    # User Logout
    url(r'^logout/$',
        logout, name='logout'),

    # User Profile
    url(r'^profile/$',
        Profile.as_view(), name='profile'),

    # User Signup
    url(r'^cadastro/$',
        Signup.as_view(), name='signup'),

    # Edit Dashboard
    url(r'editar/$',
        EditDashboard.as_view(), name='edit_dashboard'),

    # Edit Personal Info
    url(r'^editar/info_pessoal/$',
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
)
