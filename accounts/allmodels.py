# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ArFeatureResult(models.Model):
    rule = models.CharField(db_column='Rule', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    support = models.FloatField(db_column='Support', blank=True, null=True)  # Field name made lowercase.
    confidence = models.FloatField(db_column='Confidence', blank=True, null=True)  # Field name made lowercase.
    lift = models.FloatField(db_column='Lift', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'AR_Feature_result'


class ArProductResult(models.Model):
    rule = models.CharField(db_column='Rule', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    support = models.FloatField(db_column='Support', blank=True, null=True)  # Field name made lowercase.
    confidence = models.FloatField(db_column='Confidence', blank=True, null=True)  # Field name made lowercase.
    lift = models.FloatField(db_column='Lift', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'AR_Product_result'


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
        managed = False
        db_table = 'CustomerFeatures'


class Customers(models.Model):
    name = models.CharField(db_column='Name', max_length=500, blank=True, null=True)  # Field name made lowercase.
    uen = models.CharField(db_column='UEN', primary_key=True, max_length=50)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=500, blank=True, null=True)  # Field name made lowercase.
    cfu = models.CharField(db_column='CFU', max_length=500, blank=True, null=True)  # Field name made lowercase.
    genericindustry = models.CharField(db_column='GenericIndustry', max_length=500, blank=True, null=True)  # Field name made lowercase.
    industry = models.CharField(db_column='Industry', max_length=500, blank=True, null=True)  # Field name made lowercase.
    acsaccountstatus = models.CharField(db_column='ACSAccountStatus', max_length=500, blank=True, null=True)  # Field name made lowercase.
    acscreditrating = models.SmallIntegerField(db_column='ACSCreditRating', blank=True, null=True)  # Field name made lowercase.
    acrastatus = models.CharField(db_column='ACRAStatus', max_length=500, blank=True, null=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=500, blank=True, null=True)  # Field name made lowercase.
    parentcompany = models.CharField(db_column='ParentCompany', max_length=500, blank=True, null=True)  # Field name made lowercase.
    companygroup = models.CharField(db_column='CompanyGroup', max_length=500, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=500, blank=True, null=True)  # Field name made lowercase.

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


class DealsProducts(models.Model):
    matchingid = models.AutoField(db_column='MatchingID', primary_key=True)  # Field name made lowercase.
    dealid = models.ForeignKey(Deals, models.DO_NOTHING, db_column='DealID')  # Field name made lowercase.
    productname = models.ForeignKey('ProductsServices', models.DO_NOTHING, db_column='ProductName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Deals~Products'


class InitialPrice(models.Model):
    product = models.CharField(db_column='Product', max_length=100, blank=True, null=True)  # Field name made lowercase.
    otc_r = models.FloatField(db_column='OTC_R', blank=True, null=True)  # Field name made lowercase.
    otc_p = models.FloatField(db_column='OTC_P', blank=True, null=True)  # Field name made lowercase.
    otc_q = models.FloatField(db_column='OTC_Q', blank=True, null=True)  # Field name made lowercase.
    mrc_r = models.FloatField(db_column='MRC_R', blank=True, null=True)  # Field name made lowercase.
    mrc_p = models.FloatField(db_column='MRC_P', blank=True, null=True)  # Field name made lowercase.
    mrc_q = models.FloatField(db_column='MRC_Q', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Initial_Price'


class Nbinput(models.Model):
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
    purchase = models.CharField(db_column='Purchase', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NBinput'


class Nbmodel(models.Model):
    model = models.BinaryField(db_column='Model', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NBmodel'


class NbmodelAll(models.Model):
    model = models.BinaryField(db_column='Model', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NBmodel_all'


class Pic(models.Model):
    pic = models.CharField(db_column='PIC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PIC'


class Price(models.Model):
    product = models.CharField(db_column='Product', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recommended_otc = models.FloatField(db_column='Recommended_OTC', blank=True, null=True)  # Field name made lowercase.
    recommended_mrc = models.FloatField(db_column='Recommended_MRC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Price'


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
        managed = False
        db_table = 'Products/Services'


class SasBatch1(models.Model):
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    chargeamount = models.FloatField(db_column='ChargeAmount', blank=True, null=True)  # Field name made lowercase.
    listprice = models.FloatField(db_column='ListPrice', blank=True, null=True)  # Field name made lowercase.
    monthdiscountamount = models.FloatField(db_column='MonthDiscountAmount', blank=True, null=True)  # Field name made lowercase.
    monthnetrentalamount = models.FloatField(db_column='MonthNetRentalAmount', blank=True, null=True)  # Field name made lowercase.
    monthrentalamount = models.FloatField(db_column='MonthRentalAmount', blank=True, null=True)  # Field name made lowercase.
    customerclass = models.CharField(db_column='CustomerClass', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    customertype = models.CharField(db_column='CustomerType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customergroup = models.CharField(db_column='CustomerGroup', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customersector = models.CharField(db_column='CustomerSector', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pic = models.CharField(db_column='PIC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    productdescription = models.CharField(db_column='ProductDescription', max_length=500, blank=True, null=True)  # Field name made lowercase.
    uen = models.CharField(db_column='UEN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    creditrating = models.SmallIntegerField(db_column='CreditRating', blank=True, null=True)  # Field name made lowercase.
    dealid = models.AutoField(db_column='DealID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SAS-Batch 1'


class TransactionFeature(models.Model):
    sector = models.CharField(db_column='Sector', max_length=500, blank=True, null=True)  # Field name made lowercase.
    industry = models.CharField(db_column='Industry', max_length=500, blank=True, null=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=500, blank=True, null=True)  # Field name made lowercase.
    devicemanagementandmonitoring = models.CharField(db_column='DeviceManagementAndMonitoring', max_length=10, blank=True, null=True)  # Field name made lowercase.
    threatanalysis = models.CharField(db_column='ThreatAnalysis', max_length=10, blank=True, null=True)  # Field name made lowercase.
    threatdetection = models.CharField(db_column='ThreatDetection', max_length=10, blank=True, null=True)  # Field name made lowercase.
    threatresponse = models.CharField(db_column='ThreatResponse', max_length=10, blank=True, null=True)  # Field name made lowercase.
    threatintelligence = models.CharField(db_column='ThreatIntelligence', max_length=10, blank=True, null=True)  # Field name made lowercase.
    identify = models.CharField(db_column='Identify', max_length=10, blank=True, null=True)  # Field name made lowercase.
    protect = models.CharField(db_column='Protect', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Transaction_Feature'


class TransactionProduct(models.Model):
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
        managed = False
        db_table = 'Transaction_Product'


class XgbCustomerfeatures(models.Model):
    uen = models.CharField(db_column='UEN', max_length=50, blank=True, null=True)  # Field name made lowercase.
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
        managed = False
        db_table = 'XGB_CustomerFeatures'


class Xgbinput(models.Model):
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
    productname = models.CharField(db_column='ProductName', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'XGBinput'


class Xgbmodel(models.Model):
    model = models.BinaryField(db_column='Model', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'XGBmodel'


class Xgbresult(models.Model):
    uen = models.CharField(db_column='UEN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recommendedproduct = models.CharField(db_column='RecommendedProduct', max_length=500, blank=True, null=True)  # Field name made lowercase.
    application_defense = models.FloatField(db_column='Application Defense', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cloud_security = models.FloatField(db_column='Cloud Security', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    consulting_services = models.FloatField(db_column='Consulting Services', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    content_defense = models.FloatField(db_column='Content Defense', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    csi = models.FloatField(db_column='CSI', blank=True, null=True)  # Field name made lowercase.
    data_centre_security = models.FloatField(db_column='Data Centre Security', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endpoint_defense = models.FloatField(db_column='Endpoint Defense', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endpoint_security = models.FloatField(db_column='Endpoint Security', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mss_others = models.FloatField(db_column='MSS Others', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    network_defense = models.FloatField(db_column='Network Defense', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    operational_technology_security = models.FloatField(db_column='Operational Technology Security', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ot_security = models.FloatField(db_column='OT Security', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ps_others = models.FloatField(db_column='PS Others', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ps_others_bespoke_field = models.FloatField(db_column='PS Others (Bespoke)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    soc_services = models.FloatField(db_column='SOC Services', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ts_others = models.FloatField(db_column='TS Others', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ts_others_bespoke_field = models.FloatField(db_column='TS Others (Bespoke)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'XGBresult'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
