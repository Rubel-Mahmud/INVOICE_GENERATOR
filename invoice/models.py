from django.db import models
from django.utils import timezone


class Client(models.Model):

    provinces = [
        ('RANGPUR', 'Rangpur'),
        ('DHAKA', 'Dhaka'),
        ('DINAJPUR', 'Dinajpur'),
    ]

    name = models.CharField(max_length=200, verbose_name='Name')
    addressLine1 = models.CharField(max_length=200, verbose_name='Address')
    postalCode = models.CharField(max_length=20, verbose_name='Postal code')
    province = models.CharField(max_length=100, choices=provinces, verbose_name='Province')
    phoneNumber = models.CharField(max_length=100, verbose_name='Phone number')
    email = models.EmailField(max_length=200, verbose_name='Email')
    clientLogo = models.ImageField(upload_to='clientLogos/', verbose_name='Photo')

    # Utility fields
    created_at = models.DateTimeField(auto_now_add=timezone.now(), verbose_name='Created at')


    def __str__(self):
        return "{} - {}".format(self.name, self.province)


    def save(self, *args, **kwargs):
        if self.created_at == None:
            self.created_at = timezone.now()
        super(Client, self).save(*args, **kwargs)



class Invoice(models.Model):

    STATUS = [
        ('PAID', 'Paid'),
        ('UNPAID', 'Unpaid'),
        ('DUE', 'Due'),
        ('OVERDUE', 'Overdue')
    ]

    number = models.CharField(max_length=100, null=True, blank=True, verbose_name='Inv number')
    invoiceTitle = models.CharField(max_length=200, null=True, blank=True, verbose_name='Invoice title')
    dueDate = models.DateTimeField(null=True, blank=True, verbose_name='Due date')
    invoiceTotal = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name='Invoice total')
    paymentStatus = models.CharField(choices=STATUS, max_length=100, null=True, blank=True, verbose_name='Payment status')

    # Related Fields
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name='invoices', verbose_name='Client')

    # Utility Fields
    uniqueId = models.CharField(max_length=200, null=True, blank=True, verbose_name='Invoice id')
    created_at = models.DateTimeField(null=True, blank=True, verbose_name='Created at')
    last_updated = models.DateTimeField(null=True, blank=True, verbose_name='Last updated')

    def __str__(self):
        return self.number

    def save(self, *args, **kwargs):
        if self.created_at == None:
            self.created_at = timezone.now()

        self.last_updated = timezone.now()
        super(Invoice, self).save(*args, **kwargs)



class Product(models.Model):

    currency = [
        ('TK', 'TK'),
        ('USD', '$'),
        ('EUR', 'Eur'),
    ]

    productTitle = models.CharField(max_length=200, default='Product Title', verbose_name='Product name')
    description = models.TextField(max_length=4000, default='Product descriptions..', verbose_name='Description')
    quantity = models.CharField(max_length=200, default=0, verbose_name='Quantity')
    price = models.CharField(max_length=200, default=0, verbose_name='Price')
    currency = models.CharField(choices=currency, default='TK', max_length=20, verbose_name='Currency')
    image = models.ImageField(upload_to='clientLogos/', verbose_name='Product image')

    # Related Fields
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='products', verbose_name='Invoice')

    # Utility Fields
    uniqueId = models.CharField(max_length=200, verbose_name='Product id')
    created_at = models.DateTimeField(verbose_name='Created at')

    def __str__(self):
        return "{} : {}{}".format(self.productTitle, self.price, self.currency)

    def save(self, *args, **kwargs):
        if self.created_at == None:
            self.created_at = timezone.now()
        super(Product, self).save(*args, **kwargs)
