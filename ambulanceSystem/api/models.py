from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.storage import FileSystemStorage


# Create your models here.
class Ambulance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.IntegerField(null=True)
    driverName = models.CharField(max_length=30)
    healthWorker = models.IntegerField(null=True)
    oxyCylinderMeter = models.FloatField(null=True)
    severity = models.IntegerField(null=True)
    posLatitude = models.FloatField(null=True)
    posLongtude = models.FloatField(null=True)
    phoneno = models.BigIntegerField(null=True)
    hospitalName = models.CharField(max_length=30)
    person = models.IntegerField(null = True, default = 0)
    ambulanceGmeet = models.CharField(max_length=40)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Ambulance.objects.create(user=instance) 

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.ambulance.save()


class Messages(models.Model):
    hospital = models.CharField(max_length=100)
    driverName = models.CharField(max_length=50)
    meetingLink = models.CharField(max_length=50)
    solved = models.IntegerField(null=True, default = 0)
    ambulanceName = models.CharField(max_length=30, default="")
    disease = models.CharField(max_length=200, default="")
    ctv = models.IntegerField(null=True, default=0)
    oxygenPatient = models.IntegerField(null=True, default=0)


 
