from django import forms
from django.forms import ModelForm
from .models import Transaction
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div,  Submit, Reset
from django.core.exceptions import ValidationError

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

    