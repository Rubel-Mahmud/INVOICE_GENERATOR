# Generated by Django 4.0 on 2022-01-12 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0006_alter_client_clientlogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='addressLine1',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='client',
            name='clientLogo',
            field=models.ImageField(null=True, upload_to='clientLogos/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='client',
            name='postalCode',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Postal code'),
        ),
        migrations.AlterField(
            model_name='client',
            name='province',
            field=models.CharField(blank=True, choices=[('RANGPUR', 'Rangpur'), ('DHAKA', 'Dhaka'), ('DINAJPUR', 'Dinajpur')], max_length=100, null=True, verbose_name='Province'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoices', to='invoice.client', verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='dueDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Due date'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoiceTitle',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Invoice title'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoiceTotal',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Invoice total'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last updated'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Inv number'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='paymentStatus',
            field=models.CharField(blank=True, choices=[('PAID', 'Paid'), ('UNPAID', 'Unpaid'), ('DUE', 'Due'), ('OVERDUE', 'Overdue')], max_length=100, null=True, verbose_name='Payment status'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='uniqueId',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Invoice id'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(blank=True, choices=[('TK', 'TK'), ('USD', '$'), ('EUR', 'Eur')], default='TK', max_length=20, null=True, verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='Product descriptions..', max_length=4000, null=True, verbose_name='Product description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='clientLogos/', verbose_name='Product image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='invoice.invoice', verbose_name='Invoice'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productTitle',
            field=models.CharField(blank=True, default='Product Title', max_length=200, null=True, verbose_name='Product name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='product',
            name='uniqueId',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Product id'),
        ),
    ]
