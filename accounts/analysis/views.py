from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import *
import pyodbc
from .models import XGbAnalysisResult2,Xgbresult,Customers,Price,ProductsServices
from django.shortcuts import get_object_or_404

#def analysis(request):
 #   return render(request, 'analysis/analysis.html')


def analyzeCustomer(request):

    form = analyzeProductForm()

    form2 = analyzePairForm()

    return render(request,'analysis/analysis.html' ,{'form':form,'form2':form2})


def customerProductMatchAnalysis(request):

    if request.method == 'POST':

        form = analyzePairForm(request.POST)

        if form.is_valid():

            customer = get_object_or_404(Customers, uen=form.cleaned_data['customer_uen'])

            product_name = PRODUCT_CATEGORY_CHOICES[int(form.cleaned_data['product_category'])-1][1]

            products = ProductsServices.objects.filter(financiall2=product_name)

            if(int(form.cleaned_data['product_category'])<10):
                pair_analysis_result = True
            else:
                pair_analysis_result = False

            return render(request,'analysis/customerProductMatchAnalysisResult.html',
                          {'customer':customer,'products':products,'par':pair_analysis_result})#car is for customer analysis result
            #dt_instance = get_object_or_404(Xgbresult,uen=form.cleaned_data['uen'])
            #print(dt_instance.recommendedproduct)
        else:
            print("invalid form!")

    return render(request,'analysis/analysis.html')


def findProductForCustomerAnalysis(request):

    if request.method == 'POST':

        form = analyzeCustomerForm(request.POST)

        if form.is_valid():
            car = get_object_or_404(Xgbresult,uen=form.cleaned_data['uen'])
            customer = get_object_or_404(Customers,uen=form.cleaned_data['uen'])
            products = ProductsServices.objects.filter(financiall2=car.recommendedproduct)
            prices = []
            for pro in products:
                try:
                    price = Price.objects.get(product=pro.name)
                    prices.append(price)
                except Price.DoesNotExist:
                    pass
            return render(request,'analysis/analyzeCustomerResult.html',{'car':car,'customer':customer,'prices':prices})#car is for customer analysis result
            #dt_instance = get_object_or_404(Xgbresult,uen=form.cleaned_data['uen'])
            #print(dt_instance.recommendedproduct)
        else:
            print("invalid form!")

    return render(request,'analysis/analysis.html')


def findProductForCustomerNameAnalysis(request):

    if request.method == 'POST':

        form = analyzeCustomerNameForm(request.POST)

        if form.is_valid():
            customer = get_object_or_404(Customers,name=form.cleaned_data['customer_name'])
            car = get_object_or_404(Xgbresult, uen=customer.uen)
            products = ProductsServices.objects.filter(financiall2=car.recommendedproduct)
            prices = []
            for pro in products:
                try:
                    price = Price.objects.get(product=pro.name)
                    prices.append(price)
                except Price.DoesNotExist:
                    pass
            return render(request,'analysis/analyzeCustomerResult.html',{'car':car,'customer':customer,'prices':prices})#car is for customer analysis result
            #dt_instance = get_object_or_404(Xgbresult,uen=form.cleaned_data['uen'])
            #print(dt_instance.recommendedproduct)
        else:
            print("invalid form!")

    return render(request,'analysis/analysis.html')


def findCustomerForProductAnalysis(request):

    if request.method == 'POST':

        form = analyzeProductForm(request.POST)

        if form.is_valid():

            print(form.cleaned_data['product'])

            print(PRODUCT_CATEGORY_CHOICES[int(form.cleaned_data['product'])-1][1])

            return render(request,'home/home.html')#car is for customer analysis result
            #dt_instance = get_object_or_404(Xgbresult,uen=form.cleaned_data['uen'])
            #print(dt_instance.recommendedproduct)
        else:
            print("invalid form!")

    return render(request,'analysis/analysis.html')















'''

cnxn = pyodbc.connect(driver="ODBC Driver 13 for SQL Server", server="localhost\DAVIDSQL",
                          database='Singtel', uid="David_Huang", pwd="dhly1518194984@", autocommit=True)

cursor = cnxn.cursor()

cursor.execute("SELECT * FROM [Singtel].[dbo].[XGBresult] where [UEN] = 'T05SS0103A'")

result = cursor.fetchone()

temp = XGbAnalysisResult2()

temp.uen = "T05SS0103A"

temp.recommendedproduct=result[1]

temp.probability=result[11]

'''

'''
           cnxn = pyodbc.connect(driver="ODBC Driver 13 for SQL Server", server="192.168.43.95,49172",
                                 database='Singtel', uid="Singtel-IIP", pwd="IIP@Singtel123", autocommit=True)

           cursor = cnxn.cursor()

           stmt = "set nocount on; EXEC [Singtel].[dbo].[NaiveBayes] @UEN='"

           stmt+=form.cleaned_data['customer_uen']

           stmt+="',@prod='"

           stmt+=form.cleaned_data['product_category']

           stmt+="';"

           print(stmt)

           cursor.execute(stmt)

           pair_analysis_result = cursor.fetchval()
           '''

