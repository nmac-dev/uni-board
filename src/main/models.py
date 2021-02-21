from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    e_mail = models.CharField(max_length=50)
    user_name = models.CharField(max_length=30, unique=True, null=True)
    TYPE_OF_USER = (
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('A' , 'Academic'),
        ('SN', 'Support Network')
    )
    user_type = models.CharField(max_length=2, choices=TYPE_OF_USER)