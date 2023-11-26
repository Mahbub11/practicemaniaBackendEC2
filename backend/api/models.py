from django.db import models
from authuser.models import User

# Create your models here.
class Vocabulary(models.Model):
    id = models.BigAutoField(primary_key=True)
    level=models.IntegerField(default=1,blank=False, null=False)
    total_tested=models.BigIntegerField(default=0)
    type=models.IntegerField(default=1)
    inner_type=models.IntegerField(default=11)
    time=models.DecimalField(max_digits=19, decimal_places=1,default=2)
    qa=models.JSONField(encoder=None,blank=False, null=False)
    created_at=models.DateTimeField(auto_now_add=True)

class Reading(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=256,blank=True, null=True)
    explain = models.CharField(max_length=600,blank=True, null=True)
    level=models.IntegerField(default=1)
    total_tested=models.BigIntegerField(default=0)
    type=models.IntegerField(default=3)
    inner_type=models.IntegerField()
    time=models.DecimalField(max_digits=19, decimal_places=1,default=2)
    qa=models.JSONField(encoder=None,blank=False, null=False)
    created_at=models.DateTimeField(auto_now_add=True)

class Writing(models.Model):
    id = models.BigAutoField(primary_key=True)
    level=models.IntegerField(default=1)
    total_tested=models.BigIntegerField(default=0)
    type=models.IntegerField(default=2)
    inner_type=models.IntegerField()
    time=models.DecimalField(max_digits=19, decimal_places=1,default=2)
    qa=models.JSONField(encoder=None,blank=False, null=False)
    image=models.ImageField(upload_to='uploads/',blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)    

class Speaking(models.Model):
    id = models.BigAutoField(primary_key=True)
    level=models.IntegerField(default=1)
    total_tested=models.BigIntegerField(default=0)
    type=models.IntegerField(default=4)
    inner_type=models.IntegerField()
    time=models.FloatField(default=2)
    qa=models.JSONField(encoder=None,blank=False, null=False)
    image=models.ImageField(upload_to='uploads/',blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)      

class Listening(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=256,blank=True, null=True)
    level=models.IntegerField(default=1)
    total_tested=models.BigIntegerField(default=0)
    type=models.IntegerField(default=5)
    inner_type=models.IntegerField()
    time=models.DecimalField(max_digits=19, decimal_places=1,default=2)
    qa=models.JSONField(encoder=None,blank=False, null=False)
    created_at=models.DateTimeField(auto_now_add=True)

class Articals(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=256,blank=True, null=True)
    type=models.IntegerField(default=1)
    content=models.JSONField(encoder=None,blank=False, null=False)
    created_at=models.DateTimeField(auto_now_add=True) 

class StatisticDUOLINGO(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qn = models.BigIntegerField(null=True, blank=True,default=0)
    level=models.IntegerField(default=1)
    type=models.IntegerField(default=5)
    inner_type=models.IntegerField()
    time=models.DecimalField(max_digits=19, decimal_places=1)
    result=models.DecimalField(max_digits=100, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)     



   


