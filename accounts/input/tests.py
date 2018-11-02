from django.test import TestCase
from .models import Customers

# Create your tests here.
class CustomerTestCase(TestCase):
    def setUp(self):
        Customers.objects.create( name = 'CCB',  uen = 'A0162547B', # Field name made lowercase.
    sector = 'SGO-UK', # Field name made lowercase.
    cfu ='SGO',  # Field name made lowercase.
    genericindustry ='MANUFACTURING',  # Field name made lowercase.
    acsaccountstatus = 'Active',
    acscreditrating = 1,  # Field name made lowercase.
    acrastatus = 'Live',  # Field name made lowercase.
    group = 'KA',  # Field name made lowercase.
    parentcompany = 'ccb ltd',  # Field name made lowercase.
    companygroup = 'ccb pte ltd'  ,# Field name made lowercase.
    address = '998 jiaochangba road')

    def test_can_find_new_entered_customer(self):
        """Animals that can speak are correctly identified"""
        lion = Customers.objects.get(uen="A0162547B")
        self.assertEqual(lion.name, 'CCB')
