from django.urls import path
from . import views

urlpatterns = [
    path('transaction', views.make_transaction, name="make-transaction"),
    ]