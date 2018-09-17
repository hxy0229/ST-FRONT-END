from django.shortcuts import render
from django.db import connection
import pyodbc

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')

    else:
        return render(request, 'out.html')


'''
        crsr = pyodbc.connect(driver = "ODBC Driver 13 for SQL Server", server = "192.168.43.95,49172",
                              database = 'Singtel', uid = "Singtel-IIP", pwd = "IIP@Singtel123", autocommit = True)

        sql="""\
        EXEC [dbo].[NaiveBayes] @UEN = '199201623M',@prod = 'TS Others'
        """

        params1 = ('198102265N', 'CSI')
        params2 = ('199201623M', 'TS Others')

        cursor = crsr.cursor()

        cursor.execute(sql)
        return_value = cursor.fetchall()

        if (return_value == "True"):
            print("THIS COMBINATION IS GOOD!")
        else:
            print("BAD COMBINATION!")
'''


