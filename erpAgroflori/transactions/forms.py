from django import forms
from django.forms import ModelForm
from .models import Transaction, TicketSale, TicketSaleDetail
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div,  Submit, Reset
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from .models import SystemType, SystemTypeCategory

class TransactionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.user_user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.user_user:
            self.fields['user'].required = False 
            self.fields['user'].initial = self.user_user

        self.helper = FormHelper()
        self.helper.form_id = 'id-transaction_form'
        self.helper.form_class = 'transaction_form'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field('user', type='hidden'),
                Field('date', css_class='col-md-6'),
                Field('currency', css_class='col-md-6'),
                Field('method_of_payment', css_class='col-md-6'),
                Field('category', css_class='col-md-6'),
                Field('description', css_class='col-md-6'),
                Field('amount', css_class='col-md-6'),
                style="display: grid; grid-template-columns: repeat(2, 1fr);gap: 16px;"
            ),
        )
        self.helper.add_input(Submit('submit', 'Guardar'))
        self.helper.add_input(Reset('Reset This Form', 'Borrar'))

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['user'] = self.user_user
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
  
        if self.user_user is not None:
            instance.user = self.user_user
            instance.save()
            return instance
        else:
            raise ValidationError("Transaction form not linked to a user")
    

    class Meta:
        model = Transaction
        fields = ["date", "method_of_payment", "currency", "amount", "description", "category", "user"]

class TicketSaleForm(ModelForm):
    transaction = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = TicketSale
        fields = ["date", "method_of_payment", "amount"]
        #["date", "method_of_payment", "currency", "amount", "description", "category", "user"]

class CustomModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, queryset=None, *args, **kwargs):
        super(CustomModelMultipleChoiceField, self).__init__(queryset, widget=forms.SelectMultiple(), *args, **kwargs)
        id_ticket = SystemTypeCategory.objects.filter(name='ticket').first().id
        queryset =  SystemType.objects.filter(category=id_ticket)
        self.choices = [(obj.unitary_price, obj.__str__()) for obj in queryset]

class TicketSaleDetailForm(ModelForm):
    
    quantity = forms.IntegerField(widget=forms.NumberInput())
    ticket_type=CustomModelMultipleChoiceField()

    class Meta:
        model = TicketSaleDetail
        fields = ['ticket_type', 'promotion_discount', 'promotion_description' ,'ticket_sale', 'quantity'] 
    
    def __init__(self, *args, **kwargs):
        super(TicketSaleDetailForm, self).__init__(*args, **kwargs)

        category_type = 'ticket'
        id_ticket = SystemTypeCategory.objects.filter(name=category_type).first().id
        self.cat_queryset =  SystemType.objects.filter(category=id_ticket)
        self.fields['ticket_type'].queryset =self.cat_queryset
        self.fields['ticket_type'].initial = self.cat_queryset.first()
        self.fields['ticket_type'].widget.attrs['id'] = f"{self.prefix}-ticket-type"
        self.fields['quantity'].widget.attrs['id'] = f"{self.prefix}-quantity"
        self.fields['quantity'].widget.attrs['class'] = f"quantity-class"



TicketSaleFormSet = inlineformset_factory(TicketSale, TicketSaleDetail,form=TicketSaleDetailForm, exclude=[], min_num=1)

