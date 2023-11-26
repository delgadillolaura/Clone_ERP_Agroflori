from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .forms import *
from .models import *

# Create your views here.
def make_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST, **{'user':request.user})
        if form.is_valid():
            form.save(commit=True)
    else:
        form = TransactionForm()
    return render(request, "transaction.html", {"form": form})
    
def register_ticket_sale(request):
    if request.method == 'POST':
        sale_form = TicketSaleForm(request.POST, **{'user':request.user})
        formset = TicketSaleFormSet(request.POST)
        
        if sale_form.is_valid():
            ticket_sale = sale_form.save(commit=True)
            ticket_sale.transaction_ptr.category = "IN"
            ticket_sale.transaction_ptr.save()
            formset = TicketSaleFormSet(request.POST, instance=ticket_sale)
            if formset.is_valid():
                formset.save()
            else:
                TicketSale.objects.filter(id=sale_form.id).delete()
            return redirect('home')
        else:
            # Print or log form errors
            print("Form is not valid:", sale_form.errors)
    else:
        sale_form = TicketSaleForm()
        formset=TicketSaleFormSet()
    return render(request, 'ticket.html', {'sale_form': sale_form, 'formset': formset})
    