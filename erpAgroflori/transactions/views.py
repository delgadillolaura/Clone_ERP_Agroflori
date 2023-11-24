from django.shortcuts import render
from .forms import TransactionForm

# Create your views here.
def make_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST, **{'user':request.user})
        if form.is_valid():
            form.save(commit=True)
        return render(request, "transaction.html", {"form": form})
    else:
        form = TransactionForm()
        return render(request, "transaction.html", {"form": form})