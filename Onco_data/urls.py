from django.contrib import admin
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetView
from django.views.generic import TemplateView
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('data/', include('data.urls')),
    path('password-reset/', PasswordResetView.as_view(
        template_name='registration/password-reset.html'), name='password_reset'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(
        template_name='registration/password-reset-complete.html'), name='password_reset_complete'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
