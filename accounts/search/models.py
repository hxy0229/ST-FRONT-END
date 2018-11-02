from django.db import models
from .choices import *

class Customerfeatures(models.Model):
    sector = models.CharField(db_column='Sector', max_length=500, blank=True, null=True)  # Field name made lowercase.
    industry = models.CharField(db_column='Industry', max_length=500, blank=True, null=True)  # Field name made lowercase.
    creditrating = models.SmallIntegerField(db_column='CreditRating', blank=True, null=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=500, blank=True, null=True)  # Field name made lowercase.
    application_defense = models.CharField(db_column='Application Defense', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cloud_security = models.CharField(db_column='Cloud Security', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    consulting_services = models.CharField(db_column='Consulting Services', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    content_defense = models.CharField(db_column='Content Defense', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    csi = models.CharField(db_column='CSI', max_length=10)  # Field name made lowercase.
    data_centre_security = models.CharField(db_column='Data Centre Security', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endpoint_defense = models.CharField(db_column='Endpoint Defense', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endpoint_security = models.CharField(db_column='Endpoint Security', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mss_others = models.CharField(db_column='MSS Others', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    network_defense = models.CharField(db_column='Network Defense', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    operational_technology_security = models.CharField(db_column='Operational Technology Security', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ot_security = models.CharField(db_column='OT Security', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ps_others = models.CharField(db_column='PS Others', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ps_others_bespoke_field = models.CharField(db_column='PS Others (Bespoke)', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    soc_services = models.CharField(db_column='SOC Services', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ts_others = models.CharField(db_column='TS Others', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ts_others_bespoke_field = models.CharField(db_column='TS Others (Bespoke)', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = True
        db_table = 'CustomerFeatures'

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
        managed = False
        db_table = 'Customers'

class Deals(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dealno = models.CharField(db_column='DealNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customeruen = models.ForeignKey(Customers, models.DO_NOTHING, db_column='CustomerUEN', blank=True, null=True)  # Field name made lowercase.
    dealtype = models.CharField(db_column='DealType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tcv_sgd_field = models.FloatField(db_column='TCV(SGD)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    otc_sgd_field = models.FloatField(db_column='OTC(SGD)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    mrc_sgd_field = models.FloatField(db_column='MRC(SGD)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    contractperiod_months_field = models.SmallIntegerField(db_column='ContractPeriod(Months)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    probability = models.FloatField(db_column='Probability', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Deals'

class ProductsServices(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=100)  # Field name made lowercase.
    financiall1 = models.CharField(db_column='FinancialL1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    financiall2 = models.CharField(db_column='FinancialL2', max_length=500, blank=True, null=True)  # Field name made lowercase.
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

class DealsProducts(models.Model):
    matchingid = models.AutoField(db_column='MatchingID', primary_key=True)  # Field name made lowercase.
    dealid = models.ForeignKey(Deals, models.DO_NOTHING, db_column='DealID')  # Field name made lowercase.
    productname = models.ForeignKey('ProductsServices', models.DO_NOTHING, db_column='ProductName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Deals~Products'


class History(models.Model):
    deal_id = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    deal_type = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    product = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    tcv_sgd_field = models.FloatField(blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    otc_sgd_field = models.FloatField(blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    mrc_sgd_field = models.FloatField(blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    contractperiod_months_field = models.SmallIntegerField(blank=True,
                                                           null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    date = models.DateField(blank=True, null=True)

