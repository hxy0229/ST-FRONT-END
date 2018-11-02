from django.shortcuts import render,get_object_or_404
from .models import *
from django.shortcuts import HttpResponseRedirect
import pyodbc
from .forms import *

def search(request):

    form = searchProductForm()

    return render(request, 'search/search.html',{'form':form})

def searchCustomerByUEN(request):

    if request.method == 'POST':

        form = searchCustomerByUENForm(request.POST)

        if form.is_valid():

            print(form.cleaned_data['customer_uen'])

            customer = get_object_or_404(Customers,uen=form.cleaned_data['customer_uen'])

            deals = Deals.objects.filter(customeruen=customer.uen)

            histories = []

            for d in deals:
                product = DealsProducts.objects.get(dealid=d.id)
                history = History(deal_id = d.id,
                                  product = product.productname.name,
                                  deal_type = d.dealtype,
                                  tcv_sgd_field = d.tcv_sgd_field,
                                  otc_sgd_field = d.otc_sgd_field,
                                  mrc_sgd_field = d.mrc_sgd_field,
                                  contractperiod_months_field = d.contractperiod_months_field,
                                  date = d.date)
                histories.append(history)

            return render(request, 'search/customerSearchResult.html', {'customer': customer, 'histories':histories})

        else:
             print("invalid form!")

    return render(request, 'search/search.html')

def searchCustomerByName(request):

    if request.method == 'POST':

        form = searchCustomerByNameForm(request.POST)

        if form.is_valid():

            print(form.cleaned_data['customer_name'])

            if(form.cleaned_data['customer_name']=='NUS'):
                customer = get_object_or_404(Customers, name='National University of Singapore')
            elif (form.cleaned_data['customer_name'] == 'NTU'):
                customer = get_object_or_404(Customers, name='NANYANG TECHNOLOGICAL UNIVERSITY')
            else:
                customer = get_object_or_404(Customers, name=form.cleaned_data['customer_name'])

            deals = Deals.objects.filter(customeruen=customer.uen)

            histories = []

            for d in deals:
                product = DealsProducts.objects.get(dealid=d.id)
                history = History(deal_id=d.id,
                                  product=product.productname.name,
                                  deal_type=d.dealtype,
                                  tcv_sgd_field=d.tcv_sgd_field,
                                  otc_sgd_field=d.otc_sgd_field,
                                  mrc_sgd_field=d.mrc_sgd_field,
                                  contractperiod_months_field=d.contractperiod_months_field,
                                  date=d.date)
                histories.append(history)

            return render(request, 'search/customerSearchResult.html', {'customer': customer, 'histories': histories})

        else:
            print("invalid form!")

    return render(request, 'search/search.html')


def searchProduct(request):

    if request.method == 'POST':

        form = searchProductForm(request.POST)

        if form.is_valid():

            l2name = PRODUCT_CATEGORY_CHOICES[int(form.cleaned_data['product_name'])-1][1]

            print(l2name)

            products = ProductsServices.objects.filter(financiall2=l2name)

            return render(request, 'search/productSearchResult.html', {'products':products})

        else:
            print("invalid form!")

    return render(request, 'search/search.html')



'''
    if request.method == 'POST':

        cnxn = pyodbc.connect(driver="ODBC Driver 13 for SQL Server", server="localhost\DAVIDSQL",
                              database='Singtel', uid="David_Huang", pwd="dhly1518194984@", autocommit=True)

        cursor = cnxn.cursor()

        stmt=" SELECT * FROM [Singtel].[dbo].[Customers] WHERE [UEN]='T08GB0007E' "

        cursor.execute(stmt)

        result_set = cursor.fetchone()

        customer = Customers()

        #customer.name=cursor.fetchval()

        customer.name = result_set[0]
        customer.uen = result_set[1]
        customer.cfu = result_set[2]
        customer.genericindustry = result_set[4]

    else:
        return render(request,'search/search.html')

cnxn = pyodbc.connect(driver="ODBC Driver 13 for SQL Server", server="localhost\DAVIDSQL",
                              database='Singtel', uid="David_Huang", pwd="dhly1518194984@", autocommit=True)

        cursor = cnxn.cursor()

        stmt=" SELECT * FROM [Singtel].[dbo].[Customers] WHERE [UEN]='T08GB0007E' "

        cursor.execute(stmt)

        result_set = cursor.fetchone()


            history = History()

        history.deal_id = deal_result[0]
        history.product = DealsProducts.objects.get(dealid=history.deal_id).productname
        history.deal_type = deal_result[3]
        history.tcv_sgd_field = deal_result[4]
        history.otc_sgd_field = deal_result[5]
        history.mrc_sgd_field = deal_result[6]

        history.contractperiod_months_field = deal_result[7]
        history.date=deal_result[9]


'''