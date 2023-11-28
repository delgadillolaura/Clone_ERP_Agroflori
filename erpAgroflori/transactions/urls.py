from django.urls import path
from . import views

urlpatterns = [
    path('transaction', views.make_transaction, name="make-transaction"),
    path('ticket', views.register_ticket_sale, name="register-ticket-sale"),
    path('souvenir', views.register_souvenir_sale, name="register-souvenir-sale")
    ]