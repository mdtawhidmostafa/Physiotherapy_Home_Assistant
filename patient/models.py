from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class patient_list(models.Model):
    P_number = models.CharField(max_length=11,unique=True)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    gender = models.CharField(max_length=6,default=None)
    email = models.EmailField(max_length=35,blank=False,unique=True)
    contact = models.CharField(max_length=12)
    econtact = models.CharField(max_length=12)
    password = models.CharField(max_length=30,blank=False)
    address = models.CharField(max_length=200,blank=True)
    image = models.FileField(upload_to="media/patient/", max_length=250, null=True, default=None)


class patient_list_temp(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    gender = models.CharField(max_length=6,default=None)
    email = models.EmailField(max_length=35,blank=False)
    contact = models.CharField(max_length=12)
    econtact = models.CharField(max_length=12)
    password = models.CharField(max_length=30,blank=False)
    address = models.CharField(max_length=200,blank=True)
    image = models.FileField(upload_to="media/patient/", max_length=250, null=True, default=None)

class active_patient_list(models.Model):
    PID = models.CharField(max_length=11,null=True, default=None)
    pemail = models.EmailField(max_length=35,blank=False)
    pphone = models.CharField(max_length=12)
    DID = models.CharField(max_length=8,blank=False)
    RID = models.CharField(max_length=15,blank=False,unique=True)
    Date = models.DateField(null=True, default=None)


class disease_category(models.Model):
    DeID = models.CharField(max_length=8,blank=False)
    DName = models.CharField(max_length=30)
    DImage = models.FileField(upload_to="media/patient/", max_length=250, null=True, default=None)
