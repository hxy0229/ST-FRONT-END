# Generated by Django 2.1 on 2018-10-15 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('dealno', models.CharField(blank=True, db_column='DealNo', max_length=50, null=True)),
                ('dealtype', models.CharField(blank=True, db_column='DealType', max_length=50, null=True)),
                ('tcv_sgd_field', models.FloatField(blank=True, db_column='TCV(SGD)', null=True)),
                ('otc_sgd_field', models.FloatField(blank=True, db_column='OTC(SGD)', null=True)),
                ('mrc_sgd_field', models.FloatField(blank=True, db_column='MRC(SGD)', null=True)),
                ('contractperiod_months_field', models.SmallIntegerField(blank=True, db_column='ContractPeriod(Months)', null=True)),
                ('probability', models.FloatField(blank=True, db_column='Probability', null=True)),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
            ],
            options={
                'db_table': 'Deals',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DealsProducts',
            fields=[
                ('matchingid', models.AutoField(db_column='MatchingID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Deals~Products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductsServices',
            fields=[
                ('name', models.CharField(db_column='Name', max_length=100, primary_key=True, serialize=False)),
                ('financiall1', models.CharField(blank=True, db_column='FinancialL1', max_length=500, null=True)),
                ('financiall2', models.CharField(blank=True, db_column='FinancialL2', max_length=500, null=True)),
                ('financiall3', models.CharField(blank=True, db_column='FinancialL3', max_length=500, null=True)),
                ('productmanagement', models.CharField(blank=True, db_column='ProductManagement', max_length=50, null=True)),
                ('devicemanagementandmonitoring', models.CharField(blank=True, db_column='DeviceManagementAndMonitoring', max_length=10, null=True)),
                ('threatanalysis', models.CharField(blank=True, db_column='ThreatAnalysis', max_length=10, null=True)),
                ('threatdetection', models.CharField(blank=True, db_column='ThreatDetection', max_length=10, null=True)),
                ('threatresponse', models.CharField(blank=True, db_column='ThreatResponse', max_length=10, null=True)),
                ('threatintelligence', models.CharField(blank=True, db_column='ThreatIntelligence', max_length=10, null=True)),
                ('identify', models.CharField(blank=True, db_column='Identify', max_length=10, null=True)),
                ('protect', models.CharField(blank=True, db_column='Protect', max_length=10, null=True)),
                ('cost', models.FloatField(blank=True, db_column='Cost', null=True)),
            ],
            options={
                'db_table': 'Products/Services',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('name', models.CharField(blank=True, db_column='Name', max_length=500, null=True)),
                ('uen', models.CharField(db_column='UEN', max_length=50, primary_key=True, serialize=False)),
                ('sector', models.CharField(blank=True, db_column='Sector', max_length=500, null=True)),
                ('cfu', models.CharField(blank=True, db_column='CFU', max_length=500, null=True)),
                ('genericindustry', models.CharField(blank=True, db_column='GenericIndustry', max_length=500, null=True)),
                ('industry', models.CharField(blank=True, db_column='Industry', max_length=500, null=True)),
                ('acsaccountstatus', models.CharField(blank=True, db_column='ACSAccountStatus', max_length=500, null=True)),
                ('acscreditrating', models.SmallIntegerField(blank=True, db_column='ACSCreditRating', null=True)),
                ('acrastatus', models.CharField(blank=True, db_column='ACRAStatus', max_length=500, null=True)),
                ('group', models.CharField(blank=True, db_column='Group', max_length=500, null=True)),
                ('parentcompany', models.CharField(blank=True, db_column='ParentCompany', max_length=500, null=True)),
                ('companygroup', models.CharField(blank=True, db_column='CompanyGroup', max_length=500, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=500, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomerInfo',
        ),
    ]