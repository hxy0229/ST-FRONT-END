# Generated by Django 2.1 on 2018-10-29 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0004_auto_20181018_1637'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customers',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='deals',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='dealsproducts',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='productsservices',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='customers',
            table='Customers',
        ),
    ]
