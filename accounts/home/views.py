from django.shortcuts import render
from django.db import connection
import pyodbc

def home(request):

    if request.user.is_authenticated:
        '''
        cnxn = pyodbc.connect(driver="ODBC Driver 13 for SQL Server", server="192.168.43.95\49172",
                              database='Singtel', uid="Singtel-IIP", pwd="IIP@Singtel123", autocommit=True)

        cursor = cnxn.cursor()

        # cursor.execute("SELECT * from [Singtel].[dbo].[Deals]")

        cursor.execute("set nocount on; EXEC [Singtel].[dbo].[NaiveBayes] @UEN='198402868E',@prod='CSI';")

        rv = cursor.fetchval()
        print(rv)
        '''


        return render(request, 'home/home.html',{ 'dealinput':False})


    else:
      #cursor.execute("SELECT TOP (10) [ID] from [Singtel].[dbo].[Deals]")


        #return_value = cursor.fetchall()
       # for r in return_value:
           # print(r)


        return render(request, 'out.html')



        #cursor.execute("{CALL [Singtel].[dbo].[AR_Product]}")






