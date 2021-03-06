# Generated by Django 3.1 on 2020-09-13 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerCenter', '0005_auto_20200912_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.CharField(default='En attente', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.ImageField(default=None, upload_to='sellerCenter/barecode/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='Complet', max_length=200),
        ),
    ]
