# Generated by Django 2.0 on 2020-09-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing_table',
            name='Created_Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pricing_table',
            name='Updated_Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
