from django.db import models
from django.utils import timezone


class Client(models.Model):

    provinces = [
        ('RANGPUR', 'Rangpur'),
        ('DHAKA', 'Dhaka'),
        ('DINAJPUR', 'Dinajpur'),
    ]

    name = models.CharField(max_length=200, null=True, blank=True)
    addressLine1 = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=20, null=True, blank=True)
    province = models.CharField(max_length=100, choices=provinces, null=True, blank=True)
    phoneNumber = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    clientLogo = models.ImageField(upload_to='clientLogos/')

    # Utility fields
    created_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return "{} - {}".format(self.name, self.province)


    def save(self, *args, **kwargs):
        if self.created_at == None:
            self.created_at = timezone.now()
        super(Client, self).save(*args, **kwargs)



class Product(models.Model):

    currency = [
        ('TK', 'TK'),
        ('USD', '$'),
        ('EUR', 'Eur'),
    ]

    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.CharField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    currency = models.CharField(choices=currency, max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='clientLogos/', null=True, blank=True)

    # Utility Fields
    uniqueId = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return "{} : {}{}".format(self.title, self.price, self.currency)


    def save(self, *args, **kwargs):
        if self.created_at == None:
            self.created_at = timezone.now()

        super(Product, self).save(*args, **kwargs)




class Invoice(models.Model):

    STATUS = [
        ('PAID', 'Paid'),
        ('UNPAID', 'Unpaid'),
        ('DUE', 'Due'),
        ('OVERDUE', 'Overdue')
    ]

    number = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    dueDate = models.DateTimeField(null=True, blank=True)
    paymentStatus = models.CharField(choices=STATUS, max_length=100, null=True, blank=True)

    # Related Fields
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name='invoices')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')

    # Utility Fields
    uniqueId = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.number



    def save(self, *args, **kwargs):
        if self.created_at == None:
            self.created_at = timezone.now()

        super(Invoice, self).save(*args, **kwargs)

