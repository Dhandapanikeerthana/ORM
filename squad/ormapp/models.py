from django.db import models
from django.contrib import admin
class Bankloan(models.Model):
   acco=models.IntegerField(primary_key="True")
   age=models.IntegerField()
   emiinterest=models.IntegerField()
   name=models.CharField(max_length=100)
   pancard=models.IntegerField()
   mobileno=models.IntegerField()


class BankloanAdmin(admin.ModelAdmin):
  list_display=('acco','age','emiinterest','name','pancard','mobileno')
   

