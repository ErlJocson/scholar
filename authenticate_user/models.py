from django.db import models
from django.contrib.auth.models import User

class OtherInformation(models.Model):
    middle_name = models.CharField(max_length=256)
    birthday = models.DateField() 
    birth_place = models.CharField(max_length=256)
    age = models.IntegerField()
    contact = models.CharField(max_length=256)
    sex = models.CharField(max_length=256)
    civil_status = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    approved = models.BooleanField(blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class StudentEducationBackground(models.Model):
    elementary = models.CharField(max_length=256)
    school_location = models.CharField(max_length=256)
    year_graduated = models.CharField(max_length=256)
    secondary = models.CharField(max_length=256)
    school_location = models.CharField(max_length=256)
    year_graduated = models.CharField(max_length=256)
    senior_high = models.CharField(max_length=256)
    school_location = models.CharField(max_length=256)
    year_graduated = models.CharField(max_length=256)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class GuardianInformation(models.Model):
    mother_name = models.CharField(max_length=256)
    mother_ocupation = models.CharField(max_length=256)
    mother_income = models.CharField(max_length=256)
    father_name = models.CharField(max_length=256)
    father_ocupation = models.CharField(max_length=256)
    father_income = models.CharField(max_length=256)
    contact = models.CharField(max_length=256)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class StudentAdditionalInformation(models.Model):
    course = models.CharField(max_length=256)
    year_level = models.CharField(max_length=256)
    units_enrolled = models.CharField(max_length=256)
    expected_year_graduation = models.CharField(max_length=256)
    graduating = models.BooleanField()
    school_name = models.CharField(max_length=256)
    school_address = models.CharField(max_length=256)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
