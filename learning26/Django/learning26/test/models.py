from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class User(models.Model):
    ROLE_CHOICES = [
    ('seller', 'Seller'),
    ('buyer', 'Buyer'),
]
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)
    role=models.CharField(max_length=50,choices=ROLE_CHOICES,default='buyer')
    mobile=models.CharField(max_length=15)
    address=models.TextField()

    class Meta:
        db_table='user'
        verbose_name='user'
        verbose_name_plural='user'
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vin=models.CharField(max_length=17,unique=True)
    model=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    year=models.IntegerField()
    FuelType=models.CharField(max_length=50)
    
    
    class Meta:
        db_table='vehicle'
        verbose_name='vehicle'
        verbose_name_plural='vehicle'
    def __str__(self):
        return self.model

class Listing(models.Model):
    STATUS_CHOICES = [
    ('sold', 'Sold'),
    ('available', 'Available'),
]
    seller=models.ForeignKey(User,on_delete=models.CASCADE,)
    vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='available')

    class Meta:
        db_table='listing'
        verbose_name='listing'
        verbose_name_plural='listing'
    def __str__(self):
        return self.vehicle.model

class InspectionReport(models.Model):
    listing=models.ForeignKey(Listing,on_delete=models.CASCADE)
    score=models.DecimalField(max_digits=4, decimal_places=1,
    validators=[MinValueValidator(0.0),MaxValueValidator(10.0)])

    ai_summary=models.TextField()
    accidents_history=models.IntegerField()
    generated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='inspection_report'
        verbose_name='inspection_report'
        verbose_name_plural='inspection_report'
    def __str__(self):
        return self.listing.vehicle.model


class Offer(models.Model):
    STATUS_CHOICES = [
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
    ('pending', 'Pending'),
]
    listing=models.ForeignKey(Listing,on_delete=models.CASCADE)
    buyer=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')
    comment=models.TextField(null=True)

    class Meta:
        db_table='offer'
        verbose_name='offer'
        verbose_name_plural='offer'
    def __str__(self):
        return self.listing.vehicle.model

class TestDrive(models.Model):
    STATUS_CHOICES = [
    ('completed', 'Completed'),
    ('pending', 'Pending'),
    ('cancelled', 'Cancelled'),
]
    buyer=models.ForeignKey(User,on_delete=models.CASCADE)
    listing=models.ForeignKey(Listing,on_delete=models.CASCADE)
    schedule_date=models.DateTimeField()
    location=models.CharField(max_length=100)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')

    class Meta:
        db_table='testdrive'
        verbose_name='testdrive'
        verbose_name_plural='testdrive'
    def __str__(self):
        return self.listing.vehicle.model

class Transaction(models.Model):
    STATUS_CHOICES = [
    ('completed', 'Completed'),
    ('pending', 'Pending'),
    ('failed', 'Failed'),
]
    buyer=models.ForeignKey(User,on_delete=models.PROTECT)
    listing=models.ForeignKey(Listing,on_delete=models.PROTECT)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    method=models.CharField(max_length=50)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')
    date=models.DateField(auto_now_add=True)

    class Meta:
        db_table='transaction'
        verbose_name='transaction'
        verbose_name_plural='transaction'

    def __str__(self):
        return self.listing.vehicle.model