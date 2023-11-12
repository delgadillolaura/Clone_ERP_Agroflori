from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register(Transaction)
admin.site.register(SystemType)
admin.site.register(SystemTypeCategory)
admin.site.register(VolunteerPayment)
admin.site.register(Donation)
admin.site.register(FoodSale)
admin.site.register(FoodSaleDetail)
admin.site.register(SouvenirSale)
admin.site.register(SouvenirSaleDetail)
admin.site.register(TicketSale)
admin.site.register(TicketSaleDetail)
