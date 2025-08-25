from django.db import models

# Create your models here.

class dataClass(models.Model):
    firstName = models.CharField(max_length=255 , null=True)
    lastName = models.CharField(max_length=255, null=True)
    number = models.IntegerField(null=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    message = models.TextField( null=True, blank=True)
    date = models.DateField(null=True)
    
    def __str__(self):
        return self.firstName
    