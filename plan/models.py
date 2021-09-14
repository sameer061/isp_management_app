from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid
# Create your models here.
class Plan(models.Model):
    DURATION = (
        ('ONE MONTH','ONE MONTH'),
        ('SIX MONTH','SIX MONTH'),
        ('TWELVE MONTH','TWELVE MONTH'),
        ('CUSTOM','CUSTOM')
    )
    plan_name = models.CharField(max_length=200,blank=False)
    description = models.TextField(max_length=500,null=True,blank=True,help_text="enter details")
    Duration = models.TextField(choices=DURATION,default='')
    cost = models.PositiveIntegerField(blank=False)



class Userprofile(models.Model):
    user = models.CharField(max_length=200,unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email=models.EmailField(max_length=200,blank=True,null=True)
    address = models.TextField()
    profile_image=models.ImageField(blank=True,null=True, default='images/demo.jpg', upload_to='profiles')
    phoneno = PhoneNumberField(null=False, blank=False, unique=True)
    id_proof = models.FileField(upload_to='id_proof', blank=True, null=True, )
    current_plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default='')
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
  
 


