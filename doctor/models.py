from django.db import models

# Create your models here.
class doctor_list(models.Model):
    S_number = models.CharField(max_length=8,unique=True,blank=True)
    title = models.CharField(max_length=15,blank=False)
    first_name = models.CharField(max_length=25,blank=False)
    last_name = models.CharField(max_length=25)
    ltitle = models.CharField(max_length=5, default='(PT)', editable=False)
    gender = models.CharField(max_length=6)
    NIDP_number = models.CharField(max_length=18,blank=False)
    BPA_number = models.CharField(max_length=8,blank=False)
    phone = models.CharField(max_length=12,blank=False)
    ephone = models.CharField(max_length=12)
    email = models.EmailField(max_length=35,blank=False,unique=True)
    password = models.CharField(max_length=30,blank=False)
    ch_name = models.CharField(max_length=100,blank=True)
    division = models.CharField(max_length=15)
    district = models.CharField(max_length=20)
    address = models.CharField(max_length=100,blank=True)
    image = models.FileField(upload_to="doctor/", max_length=250, null=True, default=None)
    active = models.CharField(max_length=4, null=True, default="no")


class doctor_list_temp(models.Model):
    title = models.CharField(max_length=15,blank=False)
    first_name = models.CharField(max_length=25,blank=False)
    last_name = models.CharField(max_length=25)
    ltitle = models.CharField(max_length=5, default='(PT)', editable=False)
    gender = models.CharField(max_length=6)
    NIDP_number = models.CharField(max_length=18,blank=False)
    BPA_number = models.CharField(max_length=8,blank=False)
    phone = models.CharField(max_length=12,blank=False)
    ephone = models.CharField(max_length=12)
    email = models.EmailField(max_length=35,blank=False)
    password = models.CharField(max_length=30,blank=False)
    ch_name = models.CharField(max_length=100,blank=True)
    division = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    address = models.CharField(max_length=100,blank=True)
    image = models.FileField(upload_to="doctor/", max_length=250, null=True, default=None)


class exercise_list(models.Model):
    EID = models.CharField(max_length=30)
    EName = models.CharField(max_length=100)
    image = models.ImageField(upload_to='exercise/', max_length=250, null=True, default=None)
    video = models.FileField(upload_to='exercise/videos/', max_length=250, null=True, default=None)


class doctor_patient_list(models.Model):
    DID = models.CharField(max_length=8,blank=False)
    RID = models.CharField(max_length=15)
    PName = models.CharField(max_length=25,blank=False)
    PDisease = models.CharField(max_length=30,blank=False)
    PAge = models.IntegerField()
    PPhone = models.CharField(max_length=12)
    PEmail = models.CharField(max_length=35,blank=False)
    PExercise = models.CharField(max_length=100,blank=False)
    PDcategory = models.CharField(max_length=50, blank=True) 
    Date = models.DateField( null=True, default=None)
    alDID = models.CharField(max_length=8,null=True, default=None)

class DoctorDeactive(models.Model):
    DID = models.CharField(max_length=100, unique=True)
    date = models.DateField()
    time = models.TimeField()
