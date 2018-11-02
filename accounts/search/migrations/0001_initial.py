# Generated by Django 2.1 on 2018-10-29 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customerfeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(blank=True, db_column='Sector', max_length=500, null=True)),
                ('industry', models.CharField(blank=True, db_column='Industry', max_length=500, null=True)),
                ('creditrating', models.SmallIntegerField(blank=True, db_column='CreditRating', null=True)),
                ('group', models.CharField(blank=True, db_column='Group', max_length=500, null=True)),
                ('application_defense', models.CharField(db_column='Application Defense', max_length=10)),
                ('cloud_security', models.CharField(db_column='Cloud Security', max_length=10)),
                ('consulting_services', models.CharField(db_column='Consulting Services', max_length=10)),
                ('content_defense', models.CharField(db_column='Content Defense', max_length=10)),
                ('csi', models.CharField(db_column='CSI', max_length=10)),
                ('data_centre_security', models.CharField(db_column='Data Centre Security', max_length=10)),
                ('endpoint_defense', models.CharField(db_column='Endpoint Defense', max_length=10)),
                ('endpoint_security', models.CharField(db_column='Endpoint Security', max_length=10)),
                ('mss_others', models.CharField(db_column='MSS Others', max_length=10)),
                ('network_defense', models.CharField(db_column='Network Defense', max_length=10)),
                ('operational_technology_security', models.CharField(db_column='Operational Technology Security', max_length=10)),
                ('ot_security', models.CharField(db_column='OT Security', max_length=10)),
                ('ps_others', models.CharField(db_column='PS Others', max_length=10)),
                ('ps_others_bespoke_field', models.CharField(db_column='PS Others (Bespoke)', max_length=10)),
                ('soc_services', models.CharField(db_column='SOC Services', max_length=10)),
                ('ts_others', models.CharField(db_column='TS Others', max_length=10)),
                ('ts_others_bespoke_field', models.CharField(db_column='TS Others (Bespoke)', max_length=10)),
            ],
            options={
                'db_table': 'CustomerFeatures',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('name', models.CharField(blank=True, db_column='Name', max_length=500, null=True)),
                ('uen', models.CharField(db_column='UEN', max_length=50, primary_key=True, serialize=False)),
                ('sector', models.CharField(blank=True, db_column='Sector', max_length=500, null=True)),
                ('cfu', models.CharField(blank=True, db_column='CFU', max_length=500, null=True)),
                ('genericindustry', models.CharField(blank=True, choices=[(0, 'Choose industry Here...'), (1, 'ACCOMMODATION AND FOOD SERVICE ACTIVITIES'), (2, 'ACTIVITIES AUXILIARY TO FINANCIAL SERVICE AND INSURANCE ACTIVITIES'), (3, 'ACTIVITIES OF EXTRA-TERRITORIAL ORGANISATIONS AND BODIES'), (4, 'ACTIVITIES OF HEAD OFFICES; MANAGEMENT CONSULTANCY ACTIVITIES'), (5, 'ACTIVITIES OF HOUSEHOLDS AS EMPLOYERS OF DOMESTIC PERSONNEL'), (6, 'ADMINISTRATIVE AND SUPPORT SERVICE ACTIVITIES'), (7, 'ADVERTISING AND MARKET RESEARCH'), (8, 'AGRICULTURE AND FISHING'), (9, 'ARTS ENTERTAINMENT AND RECREATION'), (10, 'COMPUTER PROGRAMMING CONSULTANCY AND RELATED ACTIVITIES'), (11, 'CONSTRUCTION'), (12, 'EDUCATION'), (13, 'ELECTRICITY GAS STEAM AND AIR-CONDITIONING SUPPLY'), (14, 'FINANCIAL AND INSURANCE ACTIVITIES'), (15, 'FINANCIAL SERVICE ACTIVITIES  EXCEPT INSURANCE AND PENSION FUNDING'), (16, 'HEALTH AND SOCIAL SERVICES'), (17, 'INFORMATION AND COMMUNICATIONS'), (18, 'MANUFACTURE OF COMPUTER  ELECTRONIC AND OPTICAL PRODUCTS'), (19, 'MANUFACTURE OF MACHINERY AND EQUIPMENT'), (20, 'MANUFACTURING'), (21, 'MINING AND QUARRYING'), (22, 'OFFICE ADMINISTRATIVE  OFFICE SUPPORT AND OTHER BUSINESS SUPPORT ACTIVITIES'), (23, 'OTHER PERSONAL SERVICE ACTIVITIES'), (24, 'OTHER SERVICE ACTIVITIES'), (25, 'POSTAL AND COURIER ACTIVITIES'), (26, 'PROFESSIONAL SCIENTIFIC AND TECHNICAL ACTIVITIES'), (27, 'PUBLIC ADMINISTRATION AND DEFENCE'), (28, 'REAL ESTATE ACTIVITIES'), (29, 'RETAIL TRADE'), (30, 'TRANSPORTATION AND STORAGE'), (31, 'WAREHOUSING AND SUPPORT ACTIVITIES FOR TRANSPORTATION'), (32, 'WATER SUPPLY; SEWERAGE  WASTE MANAGEMENT AND REMEDIATION ACTIVITIES'), (33, 'WHOLESALE AND RETAIL TRADE'), (34, 'WHOLESALE TRADE'), (35, 'Others')], db_column='GenericIndustry', default=1, max_length=1, null=True)),
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
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealtype', models.CharField(blank=True, db_column='DealType', max_length=50, null=True)),
                ('tcv_sgd_field', models.FloatField(blank=True, db_column='TCV(SGD)', null=True)),
                ('otc_sgd_field', models.FloatField(blank=True, db_column='OTC(SGD)', null=True)),
                ('mrc_sgd_field', models.FloatField(blank=True, db_column='MRC(SGD)', null=True)),
                ('contractperiod_months_field', models.SmallIntegerField(blank=True, db_column='ContractPeriod(Months)', null=True)),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
            ],
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
                'managed': True,
            },
        ),
    ]
