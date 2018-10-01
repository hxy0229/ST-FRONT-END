from django.shortcuts import render
from django.db import connection
import pyodbc

def home(request):
    '''

        cnxn = pyodbc.connect(driver="ODBC Driver 13 for SQL Server", server="localhost\DAVIDSQL",
                              database='ASPNETTrial', uid="David_Huang", pwd="dhly1518194984@", autocommit=True)

        cursor = cnxn.cursor()

        #cursor.execute("SELECT TOP (10) [ID] from [Singtel].[dbo].[Deals]")

        cursor.execute("set nocount on; EXEC [Singtel].[dbo].[NaiveBayes] @UEN='198402868E',@prod='CSI';")

        rv = cursor.fetchval()
        print(rv)

        cursor.execute("SELECT TOP (10) [ID] from [Singtel].[dbo].[Deals]")


        return_value = cursor.fetchall()
        for r in return_value:
            print(r)


        #cursor.execute("{CALL [Singtel].[dbo].[AR_Product]}")
        '''

    if request.user.is_authenticated:
        return render(request, 'home.html')

    else:
        return render(request, 'out.html')




