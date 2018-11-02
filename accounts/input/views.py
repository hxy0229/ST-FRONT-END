from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import json
from .models import Customers,Deals,DealsProducts
#from django.core.context_processors import csrf
#from .forms import CustomersForm,DealsForm,DealsProductsForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import pyodbc

from .forms import *
from .choices import *
from .models import Customers,Deals,ProductsServices,DealsProducts


def input(request):

    if request.method == 'POST':

        form = inputNewDealForm(request.POST)

        if form.is_valid():

            print("valid form")

            customer = get_object_or_404(Customers, uen=form.cleaned_data['uen'])

            deal = Deals(customeruen=customer,
                         dealno=form.cleaned_data['deal_no'],
                         dealtype=DEAL_TYPE_CHOICES[int(form.cleaned_data['deal_type'])-1][1],
                         tcv_sgd_field=form.cleaned_data['total_contract_value'],
                         date=form.cleaned_data['rfs_date'])

            deal.save()

            #product = get_object_or_404(ProductsServices,financiall2=PRODUCT_CATEGORY_CHOICES[int(form.cleaned_data['product_category'])-1][1])

            product = ProductsServices.objects.filter(financiall2=PRODUCT_CATEGORY_CHOICES[int(form.cleaned_data['product_category'])-1][1])

            deal_product = DealsProducts(dealid=deal,
                                         productname=product[0])

            deal_product.save()

            print("New deal input succeed!")

            return render(request, 'home/home.html' ,{'dealinput':True})

        else:
            print("invalid form")

    else:
        form = inputNewDealForm()

    return render(request, 'input/input.html',{'form':form})






'''
def inputNewDeal(request):

    if request.method == 'POST':
        newForm = inputNewDealForm(request.POST)

        if newForm.is_valid():

            deal = Deals(CustomerUEN=newForm.uen, dealno=newForm.deal_no, DealType=newForm.deal_type,
                         tcv_sgd_field=newForm.total_contract_value, date=newForm.rfs_date)
            deal.save()

        print("New deal input succeed!")

        return render(request, 'home.html')

    else:
        newForm = inputNewDealForm()

    return render(request, 'input/input.html',{'form':newForm})


def test_print(data):
    print(data)


def searchByCustomerName(request):
    if request.method=="POST":
        search_text=request.POST['search_text']
    else:
        pass
    return HttpResponse(json.dumps())

def searchByUEN(request):
    if request.method=="POST":
        search_text=request.POST['search_text']
    else:
        pass
    return HttpResponse(json.dumps())


def createCustomer(request):
    if request.POST:
        form = PICTableform(request.POST)
        if form.is_valid:
            form.save()

            return HttpResponseRedirect('/home')
        else:
            form = PICTableform()

        args = {}
        args.update(csrf(request))

        args['form']=form           
         
         print(form.cleaned_data['total_contract_value'])

            print("INSERT INTO [Singtel].[dbo].[Deals] (DealNo,CustomerUEN,DealType,[TCV(SGD)],Date) VALUES(' " +
                             form.cleaned_data['uen'] + " ',' "+form.cleaned_data['deal_no']+" ',' "+
                             form.cleaned_data['deal_type']+" ',' "+form.cleaned_data['total_contract_value']+" ',' "+
                             form.cleaned_data['rfs_date']+" ',' ")
'''


