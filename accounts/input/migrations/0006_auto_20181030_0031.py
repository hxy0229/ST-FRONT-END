# Generated by Django 2.1 on 2018-10-29 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0005_auto_20181029_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='deals',
            name='customeruen',
            field=models.ForeignKey(blank=True, db_column='CustomerUEN', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='input.Customers'),
        ),
        migrations.AddField(
            model_name='dealsproducts',
            name='dealid',
            field=models.ForeignKey(db_column='DealID', default='2222', on_delete=django.db.models.deletion.DO_NOTHING, to='input.Deals'),
        ),
        migrations.AddField(
            model_name='dealsproducts',
            name='productname',
            field=models.ForeignKey(db_column='ProductName', default='SOME STRING', on_delete=django.db.models.deletion.DO_NOTHING, to='input.ProductsServices'),
        ),
        migrations.AlterField(
            model_name='deals',
            name='dealtype',
            field=models.CharField(blank=True, choices=[(1, 'Upgrade'), (2, 'Downgrade'), (3, 'New'), (4, 'Win-back'), (5, 'Termination'), (6, 'Renewal'), (7, 'Others')], db_column='DealType', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='productsservices',
            name='financiall2',
            field=models.CharField(blank=True, choices=[(1, 'Application Defense'), (2, 'Cloud Security'), (3, 'Consulting Services'), (4, 'Content Defense'), (5, 'CSI'), (6, 'Data Centre Security'), (7, 'Endpoint Defense'), (8, 'Endpoint Security'), (9, 'MSS Others'), (10, 'Network Defense'), (11, 'Operational Technology Security'), (12, 'OT Security'), (13, 'PS Others'), (14, 'PS Others (Bespoke)'), (15, 'TS Others'), (16, 'TS Others (Bespoke)')], db_column='FinancialL2', max_length=1, null=True),
        ),
    ]
