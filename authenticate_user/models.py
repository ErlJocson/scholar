from django.db import models
from django.contrib.auth.models import User

class OtherInformation(models.Model):
    middle_name = models.CharField(256)
    birthday = models.DateField() 
    birth_place = models.CharField(256)
    age = models.IntegerField()
    contact = models.CharField(256)
    sex = models.CharField(256)
    civil_status = models.CharField(256)
    address = models.CharField(256)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class StudentEducationBackground(models.Model):
    elementary = models.CharField(256)
    school_location = models.CharField(256)
    year_graduated = models.CharField(256)
    secondary = models.CharField(256)
    school_location = models.CharField(256)
    year_graduated = models.CharField(256)
    senior_high = models.CharField(256)
    school_location = models.CharField(256)
    year_graduated = models.CharField(256)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class StudentBackgroundEducation(models.Model):
    mother_name = models.CharField(256)
    mother_ocupation = models.CharField(256)
    mother_income = models.CharField(256)
    father__name = models.CharField(256)
    father_ocupation = models.CharField(256)
    father_income = models.CharField(256)
    contact = models.CharField(256)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class StudentAdditionalInformation(models.Model):
    course = models.CharField(256)
    year_level = models.CharField(256)
    units_enrolled = models.CharField(256)
    expected_year_graduation = models.CharField(256)
    graduating = models.BooleanField()
    school_name = models.CharField(256)
    school_address = models.CharField(256)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
