# Generated by Django 5.1.1 on 2024-09-23 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='order_no',
            field=models.CharField(default='ORD000000', help_text='Order number associated with the product.', max_length=50),
        ),
        migrations.AddField(
            model_name='productdetails',
            name='warranty_till',
            field=models.DateField(default=datetime.date.today, help_text='Date till the product warranty is valid.'),
        ),
    ]
