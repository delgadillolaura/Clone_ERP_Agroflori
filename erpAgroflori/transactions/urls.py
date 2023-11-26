from django.urls import path
from . import views

urlpatterns = [
    path('transaction', views.make_transaction, name="make-transaction"),
    path('ticket', views.register_ticket_sale, name="register-ticket-sale"),
    path('search-transaction/', views.TransactionListView.as_view(), name="search-transactions"),
    path('update-transaction/<int:pk>', views.TransactionUpdateView.as_view(), name="update-transaction"),
    ]