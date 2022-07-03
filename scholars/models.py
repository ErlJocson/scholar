from django.db import models
from django.contrib.auth.models import User

class RegistrationForm(models.Model): 
    image = models.FileField(upload_to="media/registrations")
    approved = models.CharField(max_length=20, choices=(('For checking', 'For checking'),('Approved', 'Approved'),('Disapproved', 'Disapproved')), default='For checking')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class ParentsVotersID(models.Model): 
    image = models.FileField(upload_to="media/parents")
    approved = models.CharField(max_length=20, choices=(('For checking', 'For checking'),('Approved', 'Approved'),('Disapproved', 'Disapproved')), default='For checking')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
class ScholarVotersID(models.Model): 
    image = models.FileField(upload_to="media/scholars")
    approved = models.CharField(max_length=20, choices=(('For checking', 'For checking'),('Approved', 'Approved'),('Disapproved', 'Disapproved')), default='For checking')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class CopyOfGrades(models.Model): 
    image = models.FileField(upload_to="media/grades")
    approved = models.CharField(max_length=20, choices=(('For checking', 'For checking'),('Approved', 'Approved'),('Disapproved', 'Disapproved')), default='For checking')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class ProfilePicture(models.Model):
    image = models.ImageField(upload_to="pictures")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class KiloOfPlastic(models.Model):
    kilo = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class DateOfGrants(models.Model):
    date = models.DateField()
    show = models.BooleanField(default=True)