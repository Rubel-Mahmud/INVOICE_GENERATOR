from django.db import models
from uuid import uuid4
from django.template.defaultfilters import slugify
from django.utils import timezone


class Client(models.Model):

    PROVINCES = [
        ('RANGPUR', 'rangpur'),
        ('DHAKA', 'dhaka'),
        ('CHITTAGONG', 'chittagong'),
        ('DINAJPUR', 'dinajpur'),
    ]

    # Basic fields
    clientName = models.CharField(max_length=200, null=True, blank=True)
    addressLine1 = models.CharField(max_length=200, null=True, blank=True)
    clientLogo = models.ImageField(default='default_image.jpg', upload_to='company_logos')
    postalCode = models.CharField(max_length=10, null=True, blank=True)
    phoneNumber = models.CharField(max_length=50, null=True, blank=True)
    province = models.CharField(max_length=100, choices=PROVINCES, blank=True)
    emailAddress = models.CharField(max_length=100, null=True, blank=True)
    taxNumber = models.CharField(max_length=200, null=True, blank=True)

    # Utility fields
    uniqueId = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=500, unique=True, null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return '{} {} {}'.format(self.clientName, self.province, self.uniqueId)


    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-'[4])
            self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Client, self).save(*args, **kwargs)




class Product(models.Model):

    CURRENCY = [
        ('TK', 'TK'),
        ('$', 'USD'),
    ]

    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    currency = models.CharField(choices=CURRENCY, default='TK', null=True)
    productImage = models.FileField(upload_to=None, max_length=200, null=True, blank=True)

    # Utility fields
    uniqueId = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)


    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug':self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())

        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Product, self).save(*args, **kwargs)




class Invoice(models.Model):

    TERMS = [
    ('14 days', '14 days'),
    ('30 days', '30 days'),
    ('60 days', '60 days'),
    ]

    STATUS = [
    ('CURRENT', 'CURRENT'),
    ('OVERDUE', 'OVERDUE'),
    ('PAID', 'PAID'),
    ]

    title = models.CharField(max_length=200, null=True, blank=True)
    number = models.CharField(max_length=200, null=True, blank=True)
    dueDate = models.DateField(null=True, blank=True)
    paymentTerms = models.CharField(choices=TERMS, null=True, blank=True)
    status = models.CharField(max_length=200, choices=STATUS, default='CURRENT')
    note = models.TextField(null=True, blank=True)


    # Related fields
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL)

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)


    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug':self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())

        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify()

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Invoice, self).save(*args, **kwargs)






class Settings(models.Model):

    PROVINCES = [
        ('RANGPUR', 'rangpur'),
        ('DHAKA', 'dhaka'),
        ('CHITTAGONG', 'chittagong'),
        ('DINAJPUR', 'dinajpur'),
    ]

    # Basic fields
    clientName = models.CharField(max_length=200, null=True, blank=True)
    addressLine1 = models.CharField(max_length=200, null=True, blank=True)
    clientLogo = models.ImageField(default='default_image.jpg', upload_to='company_logos')
    postalCode = models.CharField(max_length=10, null=True, blank=True)
    phoneNumber = models.CharField(max_length=50, null=True, blank=True)
    province = models.CharField(max_length=100, choices=PROVINCES, blank=True)
    emailAddress = models.CharField(max_length=100, null=True, blank=True)
    taxNumber = models.CharField(max_length=200, null=True, blank=True)

    # Utility fields
    uniqueId = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=500, unique=True, null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return '{} {} {}'.format(self.clientName, self.province, self.uniqueId)


    def get_absolute_url(self):
        return reverse('settings-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-'[4])
            self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Settings, self).save(*args, **kwargs)
