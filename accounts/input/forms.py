from django import forms
from .choices import *
from .models import Customers, Deals, DealsProducts
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class inputNewDealForm(forms.Form):
    customer_name = forms.CharField(label="Customer Name",
                                    error_messages={'required': 'Please enter customer name'})
    uen = forms.CharField(required=True, label="UEN",
                          error_messages={'required': 'Please enter the Unique Entity Number of the customer'})
    cfu = forms.ChoiceField(label="Customer Facing Unit",choices=CFU_CHOICES,
                          error_messages={'required': 'Please enter the customer facing unit'})
    generic_industry = forms.ChoiceField(label="Generic Industry",
                                        choices= GENERIC_INDUSTRY_CHOICES,
                                       error_messages={'invalid_choice':0})

    deal_type = forms.ChoiceField(required=True, label="Deal Type",  choices= DEAL_TYPE_CHOICES)
    deal_no = forms.CharField(required=True, label="Deal Number", error_messages={'required': 'Please enter the deal number'})
    contract_mode = forms.ChoiceField(required=True, label = "Contract Mode", choices= CONTRACT_MODE_CHOICES)
    total_contract_value = forms.CharField(required=True, label="Total Contract Value(SGD)", error_messages={'required': 'Please enter total contract value of this deal'})


    product_category=forms.ChoiceField(required=True, label = "Product",  choices=PRODUCT_CATEGORY_CHOICES)
    rfs_date = forms.DateField(required=True, label = "RFS Date", error_messages={'required': 'Please enter an rfs date', 'invalid': 'Please enter a valid rfs date'})


    #def is_valid(self):
        #return (self.clean_customer_data() and self.clean_deal_data() and self.clean_product_data())


'''
class CustomersForm(forms.ModelForm):

    class Meta:
        model = Customers

class DealsForm(forms.ModelForm):

    class Meta:
        model = Deals

class DealsProductsForm(forms.ModelForm):

    class Meta:
        model = DealsProducts
'''

