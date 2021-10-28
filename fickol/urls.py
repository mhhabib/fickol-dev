"""fickol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('root/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.login, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('reset_passord/', auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
         name="reset_password"),
    path('reset_passord_sent/', auth_views.PasswordResetDoneView.as_view(template_name="users/reset_passord_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_passord_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_done.html"),
         name="password_reset_complete"),
    path('', include('f_home.urls')),

]
handler404 = 'users.views.not_found_view'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
