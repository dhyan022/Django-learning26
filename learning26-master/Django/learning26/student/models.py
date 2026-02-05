from django.db import models
# Create your models here.

class Student(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=50)
    studentEmail = models.EmailField(max_length=254)

    class Meta:
        db_table = "student"


class product(models.Model):
    productName=models.CharField(max_length=50)
    productPrice=models.IntegerField()
    productDescription=models.TextField()
    productStock=models.IntegerField()
    productColor=models.CharField(null=True)
    proudctStatus=models.BooleanField(default=True)

    class Meta:
        db_table = "product"



class movie(models.Model):
    Name=models.CharField( max_length=50)
    showTime=models.CharField(max_length=20)
    # showTime=models.TimeField(auto_now=False, auto_now_add=False)
    ticketPrice=models.PositiveIntegerField()
    MovieStory=models.TextField()

    class Meta:
        db_table='Movies'