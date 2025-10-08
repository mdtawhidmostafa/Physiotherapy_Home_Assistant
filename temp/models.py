from django.db import models


class ResultEx(models.Model):
    rid = models.CharField(max_length=100)  # Random number 1-99
    eid = models.CharField(max_length=10)
    result = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    video_duration = models.FloatField()
    time = models.CharField(max_length=100,null=True,default=None)

from patient.models import patient_list

class Notification(models.Model):
    recipient = models.ForeignKey(patient_list, on_delete=models.CASCADE)
    message = models.TextField()
    notification_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)   

class Notificationes2(models.Model):
    RID = models.CharField(max_length=100, unique=False)  # Allow duplicate values
    DID = models.CharField(max_length=100, null=True, default=None, unique=False)
    message = models.TextField()
    notification_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(unique=False) 
    created_date = models.DateField(unique=False)
    created_time = models.TimeField(unique=False)
    read = models.BooleanField(default=False)  
  

class NoteExercise2(models.Model):
    RID = models.CharField(max_length=100, unique=False)  # Allow duplicate values
    DID = models.CharField(max_length=100, null=True, default=None, unique=False)
    message = models.TextField()
    notification_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(unique=False) 
    created_date = models.DateField(unique=False)
    created_time = models.TimeField(unique=False)


