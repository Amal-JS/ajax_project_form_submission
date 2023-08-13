from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Sample(models.Model):

    #validation functions to check if name has length <5 and  name contains 'a' 
    def name_check(value):
        if 'a' in value:
            raise ValidationError("Name with 'a' not allowed")
        return value
    def name_check_len(value):
        if len(value)<5:
            raise ValidationError("Name should be atleast 5 characters")
    
    name= models.CharField(max_length=30,validators=[name_check,name_check_len])
    email = models.EmailField()


    def __str__(self) :
        return self.name
    
  