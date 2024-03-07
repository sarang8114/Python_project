from django.db import models

# Create your models here.

class Donor(models.Model):
    firstName = models.CharField(max_length=15,default='f_name')
    middleName = models.CharField(max_length=15,default='m_name')
    lastName = models.CharField(max_length=15,default='l_name')
    ageOfDonor = models.IntegerField(default='50')
    contact_number = models.CharField(max_length=15,default='1234567891')
    emailIdOfDonor = models.CharField(max_length=20,default='email')
    addressOfDonor = models.CharField(max_length=100,default='India')
    genderOfDonor = models.CharField(max_length=10,default='Female')
    bloodGrp = models.CharField(max_length=5,default='O+')
    organ_to_donate = models.CharField(max_length=10,default='Heart')

    def _str_(self):
        return self.firstName
