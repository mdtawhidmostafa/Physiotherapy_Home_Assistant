from django.db import models

class admin_list(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    gender = models.CharField(max_length=6,null=True, default=None)
    email = models.EmailField(max_length=35,blank=False,unique=True)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=30,blank=False)
    category = models.CharField(max_length=30,blank=False)
    image = models.FileField(upload_to="media/Admin/", max_length=250, null=True, default=None)
