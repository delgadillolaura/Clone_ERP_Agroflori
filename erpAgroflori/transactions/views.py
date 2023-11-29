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
    

def register_souvenir_sale(request):
    if request.method == 'POST':
        sale_form = SouvenirSaleForm(request.POST, **{'user':request.user})
        formset = SouvenirSaleFormSet(request.POST)
        
        if sale_form.is_valid():
            souvenir_sale = sale_form.save(commit=True)
            formset = SouvenirSaleFormSet(request.POST, instance=souvenir_sale)
            if formset.is_valid():
                formset.save()
            else:
                SouvenirSale.objects.filter(id=sale_form.id).delete()
            return redirect('home')
        else:
            # Print or log form errors
            print("Form is not valid:", sale_form.errors)
    else:
        sale_form = SouvenirSaleForm()
        formset=SouvenirSaleFormSet()
    return render(request, 'souvenir.html', {'sale_form': sale_form, 'formset': formset})

def register_food_sale(request):
    if request.method == 'POST':
        sale_form = FoodSaleForm(request.POST, **{'user':request.user})
        formset = FoodSaleFormSet(request.POST)
        
        if sale_form.is_valid():
            food_sale = sale_form.save(commit=True)
            formset = FoodSaleFormSet(request.POST, instance=food_sale)
            if formset.is_valid():
                formset.save()
            else:
                FoodSale.objects.filter(id=sale_form.id).delete()
            return redirect('home')
        else:
            # Print or log form errors
            print("Form is not valid:", sale_form.errors)
    else:
        sale_form = FoodSaleForm()
        formset=FoodSaleFormSet()
    return render(request, 'food.html', {'sale_form': sale_form, 'formset': formset})