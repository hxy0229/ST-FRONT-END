from django import forms
from .choices import *

class analyzeCustomerForm(forms.Form):
    uen = forms.CharField(label="UEN", max_length=50,error_messages={'required': 'Please enter customer name'})

class analyzeCustomerNameForm(forms.Form):
    customer_name = forms.CharField(label="UEN", max_length=50,error_messages={'required': 'Please enter customer name'})

class analyzePairForm(forms.Form):
    customer_uen = forms.CharField(label="UEN", max_length=50,error_messages={'required': 'Please enter customer name'})
    product_category = forms.ChoiceField(required=True, label="Product",choices=PRODUCT_CATEGORY_CHOICES)

class analyzeProductForm(forms.Form):
    product = forms.ChoiceField(required=True, label="Product",choices= PRODUCT_CATEGORY_CHOICES)


