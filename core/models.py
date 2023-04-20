from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='User')
    firstname = models.TextField(max_length=20, default='Firstname')
    middlename = models.TextField(max_length=20, default='Middlename')
    lastname = models.TextField(max_length=20, default='Lastname')
    email = models.EmailField(default='user@email.com')
    age = models.IntegerField(default='10')

    def __str__(self):
        return self.user.username
    
status_choice = (('approved', 'APPROVED'), ('pending', 'PENDING'), ('rejected', 'REJECTED'))

region_choice = (('ahafo', 'Ahafo Region'), ('ashanti', 'Ashanti Region'), ('bono', 'Bono East Region'),
                 ('brong', 'Brong Ahafo Region'), ('central', 'Central Region'), ('eastern', 'Eastern Region'),
                 ('greater', 'Greater Accra Region'), ('north east', 'North East Region'), ('northern', 'Northern Region'),
                 ('oti', 'Oti Region'), ('savannah', 'Savannah Region'), ('upper east', 'Upper East Region'),
                 ('upper west', 'Upper West Region'), ('western', 'Western Region'), ('western north', 'Western North Region'),
                 ('volta', 'Volta Region'))

class Donor(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    firstname = models.TextField(max_length=30, default='')
    middlename = models.TextField(max_length=30, default='')
    lastname = models.TextField(max_length=30, default='')
    email = models.CharField(default='', max_length=50)
    phone_number = models.CharField(max_length=10, default='##########')
    region = models.CharField(max_length=30, choices= region_choice, default='ahafo')
    area_or = models.TextField(default='Area')
    town = models.TextField(default='')
    id_number = models.CharField(default='GHA-###########-1', max_length=30)
    donor_number = models.IntegerField(default=0)
    donor_card = models.CharField(default='NBS/20/##########/', max_length=30)
    name_of_patient = models.TextField(max_length=200, default='')
    hospital = models.CharField(max_length=200, default='')
    ward = models.CharField(max_length=10, default='Ward #')
    status = models.CharField(max_length=10, choices = status_choice, default='pending')
