# Generated by Django 4.0 on 2022-01-10 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='clientLogo',
            field=models.ImageField(null=True, upload_to='clientLogos/'),
        ),
    ]