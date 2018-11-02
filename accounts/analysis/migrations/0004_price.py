# Generated by Django 2.1 on 2018-10-30 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_auto_20181030_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('product', models.CharField(db_column='Product', max_length=100, primary_key=True, serialize=False)),
                ('recommended_otc', models.FloatField(blank=True, db_column='Recommended_OTC', null=True)),
                ('recommended_mrc', models.FloatField(blank=True, db_column='Recommended_MRC', null=True)),
            ],
            options={
                'db_table': 'Price',
                'managed': False,
            },
        ),
    ]
