from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Trackerdata(models.Model):
    user =models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE)
    automation =models.CharField(max_length =120)
    task = models.CharField(max_length =120)
    stardate= models.DateField(auto_now=False, auto_now_add=False)
    enddate =models.DateField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length =24, blank=True)
    blockers = models.CharField(max_length =120,blank=True)
    spoc = models.CharField(max_length =24,blank=True)
    finished=models.BooleanField(default= False,blank=True)

    def __str__(self):
        return self.automation 
