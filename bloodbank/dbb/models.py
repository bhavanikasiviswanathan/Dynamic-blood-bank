from django.db import models

# Create your models here.

class Bloodbank(models.Model):
	name 	 = models.CharField(max_length = 120)
	location = models.CharField(max_length = 120,null= True, blank = False)

class Donor(models.Model):
	name 		 	= 	models.CharField(max_length = 120)
	location 	 	= 	models.CharField(max_length = 120, null = True, blank = False)
	date_of_birth 	= 	models.DateField(null = True, blank = False)
class User(models.Model):
	username 		= 	models.CharField(max_length=120)
	email 	    	= 	models.EmailField(max_length=70,blank=True)
	password		=	models.CharField(max_length=120)
	confirmpassword	=	models.CharField(max_length=120)