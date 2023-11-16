from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.register, name="registration"),
    path('complete-registration/<username>', views.complete_registration, name="complete-registration"),
    path('login/', views.authenticate_user, name="authenticate")
]