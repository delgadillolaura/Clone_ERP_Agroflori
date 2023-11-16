from django.urls import path
from . import views
import erpAgroflori.settings as settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.redirect_log_in, name="redirect-log-in"),
    path('registration/', views.register, name="registration"),
    path('complete-registration/<username>', views.complete_registration, name="complete-registration"),
    path('login/', views.authenticate_user, name="log-in"),
    path('logout/', views.logout_view, name='log-out'),
]