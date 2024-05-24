"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from firstapp.views import (
     TokenObtainPairView,
    TokenRefreshView,PasswordResetView, PasswordResetConfirmView )
from django.contrib.auth import views as auth_views
from task_management import views
from django.urls import path
from django.urls import path
urlpatterns = [
     path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/',include('firstapp.urls')),
    path('api/password/reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('password/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('api/',include('task_management.urls')),


]