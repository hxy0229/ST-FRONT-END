from django.db import models

class Xgbresult(models.Model):
    uen = models.CharField(db_column='UEN', max_length=50,primary_key=True)  # Field name made lowercase.
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

class XGbAnalysisResult2(models.Model):
    uen = models.CharField(db_column='UEN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recommendedproduct = models.CharField(db_column='RecommendedProduct', max_length=500, blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)

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


class Price(models.Model):
    product = models.CharField(db_column='Product', max_length=100, primary_key=True)  # Field name made lowercase.
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






