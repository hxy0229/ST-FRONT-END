from django.db import models
from .choices import *


class Customers(models.Model):
    name = models.CharField(db_column='Name', max_length=500, blank=True, null=True)  # Field name made lowercase.
    uen = models.CharField(db_column='UEN', primary_key=True, max_length=50)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=500, blank=True, null=True)  # Field name made lowercase.
    cfu = models.CharField(db_column='CFU', max_length=500, blank=True, null=True)  # Field name made lowercase.
    genericindustry = models.CharField(db_column='GenericIndustry', choices=GENERIC_INDUSTRY_CHOICES, max_length=1, default=1,blank=True, null=True)  # Field name made lowercase.
    industry = models.CharField(db_column='Industry', max_length=500, blank=True, null=True)  # Field name made lowercase.
    acsaccountstatus = models.CharField(db_column='ACSAccountStatus', max_length=500, blank=True, null=True)  # Field name made lowercase.
    acscreditrating = models.SmallIntegerField(db_column='ACSCreditRating', blank=True, null=True)  # Field name made lowercase.
    acrastatus = models.CharField(db_column='ACRAStatus', max_length=500, blank=True, null=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=500, blank=True, null=True)  # Field name made lowercase.
    parentcompany = models.CharField(db_column='ParentCompany', max_length=500, blank=True, null=True)  # Field name made lowercase.
    companygroup = models.CharField(db_column='CompanyGroup', max_length=500, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Customers'


class Deals(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dealno = models.CharField(db_column='DealNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customeruen = models.ForeignKey(Customers, models.DO_NOTHING, db_column='CustomerUEN', blank=True, null=True)  # Field name made lowercase.
    dealtype = models.CharField(db_column='DealType', choices=DEAL_TYPE_CHOICES,  max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcv_sgd_field = models.FloatField(db_column='TCV(SGD)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    otc_sgd_field = models.FloatField(db_column='OTC(SGD)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    mrc_sgd_field = models.FloatField(db_column='MRC(SGD)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    contractperiod_months_field = models.SmallIntegerField(db_column='ContractPeriod(Months)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    probability = models.FloatField(db_column='Probability', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Deals'


class DealsProducts(models.Model):
    matchingid = models.AutoField(db_column='MatchingID', primary_key=True)  # Field name made lowercase.
    dealid = models.ForeignKey(Deals, models.DO_NOTHING, db_column='DealID',default='2222')  # Field name made lowercase.
    productname = models.ForeignKey('ProductsServices', models.DO_NOTHING, db_column='ProductName',default='SOME STRING')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Deals~Products'

class ProductsServices(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=100)  # Field name made lowercase.
    financiall1 = models.CharField(db_column='FinancialL1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    financiall2 = models.CharField(db_column='FinancialL2', choices=PRODUCT_CATEGORY_CHOICES, max_length=1, blank=True, null=True)  # Field name made lowercase.
    financiall3 = models.CharField(db_column='FinancialL3', max_length=500, blank=True, null=True)  # Field name made lowercase.
    productmanagement = models.CharField(db_column='ProductManagement', max_length=50, blank=True, null=True)  # Field name made lowercase.
    devicemanagementandmonitoring = models.CharField(db_column='DeviceManagementAndMonitoring', max_length=10, blank=True, null=True)  # Field name made lowercase.
    threatanalysis = models.CharField(db_column='ThreatAnalysis', max_length=10, blank=True, null=True)  # Field name made lowercase.
    threatdetection = models.CharField(db_column='ThreatDetection', max_length=10, blank=True, null=True)  # Field name made lowercase.
    threatresponse = models.CharField(db_column='ThreatResponse', max_length=10, blank=True, null=True)  # Field name made lowercase.
    threatintelligence = models.CharField(db_column='ThreatIntelligence', max_length=10, blank=True, null=True)  # Field name made lowercase.
    identify = models.CharField(db_column='Identify', max_length=10, blank=True, null=True)  # Field name made lowercase.
    protect = models.CharField(db_column='Protect', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Products/Services'


