from django.db import models

# Create your models here.
class Patient(models.Model):
    name= models.CharField(max_length=100)
    age= models.IntegerField()
    email= models.EmailField()
    phone=models.CharField(max_length=15)
    message= models.TextField()
    date= models.DateField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name= models.CharField(max_length=50)
    age= models.IntegerField()
    email= models.EmailField()
    department=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class staff(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    position=models.CharField(max_length=30)
    hire=models.DateField()

    def __str__(self):
        return self.firstname + " " + self.lastname

class ward(models.Model):
    name=models.CharField(max_length=30)
    beds=models.IntegerField()
    available=models.IntegerField()

    def __str__(self):
        return self.name

class appointment(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    date=models.DateTimeField()
    department=models.CharField(max_length=50)
    doctor=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.name

class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.name
