"""
Definition of models.
"""

from django.db import models
from django.core.validators import MaxLengthValidator

# Model about me
class Me(models.Model):
	Name = models.CharField(max_length = 30)
	Last_name = models.CharField(max_length = 30)
	Date_of_birth = models.DateField()
	# Contacts
	Email = models.EmailField(max_length=30,blank=True)
	Jabber = models.EmailField(max_length=30,blank=True)
	Skype = models.CharField(max_length = 30)
	# Other contacts
	Other_contacts = models.TextField(validators=[MaxLengthValidator(200)])
	Bio = models.TextField(validators=[MaxLengthValidator(200)])
	

