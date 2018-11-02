from django import forms
from .choices import *

class searchCustomerByUENForm(forms.Form):
    customer_uen = forms.CharField(label="UEN", max_length=500, error_messages={'required': 'Please enter customer name'})

class searchCustomerByNameForm(forms.Form):
    customer_name= forms.CharField(label="UEN", max_length=500, error_messages={'required': 'Please enter customer name'})

class searchProductForm(forms.Form):
    product_name = forms.ChoiceField(required=True, label="Product",choices= PRODUCT_CATEGORY_CHOICES)


