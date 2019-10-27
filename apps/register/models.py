from __future__ import unicode_literals
from django.db import models
from django import forms

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['first_name'].isalpha()) == False:
            if len(postData['first_name']) <=2:
                errors['first_name'] = "First name can not be shorter than 2 characters"

        if (postData['last_name'].isalpha()) == False:
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last name can not be shorter than 2 characters"

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"

        if len(postData['password']) < 10:
            errors['password'] = "Password is too short!"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255,)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()


from django.db import models
from datetime import date






class Doctor(models.Model):
    firstName = models.CharField(max_length=50, default='')
    lastName = models.CharField(max_length=50, default='')
    username = models.CharField(max_length=30, default='')
    field = models.CharField(max_length=20,default="")
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE,)


    def __str__(self):
        return self.firstName + " " + self.lastName



class Patient(models.Model):
    firstName = models.CharField(max_length=50, default='')
    lastName = models.CharField(max_length=50, default='')
    number = models.CharField(max_length=13, default='')
    address = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=23, default='')
    weight = models.CharField(max_length=6, default='')
    previous_symptoms=models.CharField(max_length=12,default='')
    allergies = models.TextField(max_length=500, default='')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE,)



#
# class Nurse(models.Model):
#     firstName = models.CharField(max_length=50, default='')
#     lastName = models.CharField(max_length=50, default='')
#     username = models.CharField(max_length=30, default='')
#     partytime = models.DateTimeField()
#     def __str__(self):
#         return self.firstName + " " + self.lastName
#



class Administrator(models.Model):
    firstName = models.CharField(max_length=50, default='')
    lastName = models.CharField(max_length=50, default='')
    # username = models.CharField(max_length=30, default='')
    # user = models.ForeignKey(User, null=True, on_delete=models.CASCADE,)
    def __str__(self):
        return self.firstName + " " + self.lastName




# class Prescription(models.Model):
#     name = models.CharField(max_length=50, default='')
#     patient = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE,)
#     doctor = models.ForeignKey(Doctor, null=True, on_delete=models.CASCADE,)
#     dosage = models.CharField(max_length=100,   )
#
#     def __str__(self):
#         return self.name
#
#     def getPatient(self, pre):
#         return pre.patient
#
#     def getDoctor(self, pre):
#         return pre.doctor




class Test(models.Model):
    testResults = models.FileField(upload_to='tests', null=True, blank=True)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE,)
    doctor = models.ForeignKey(Doctor, null=True,   on_delete=models.CASCADE,)
    def __str__(self):
        return self.name

    def getPatient(self, test):
        return test.patient

    def getDoctor(self, test):
        return test.doctor



class Appointment(models.Model):
    month = models.CharField(max_length=2, default='')
    day = models.CharField(max_length=2, default='')
    year = models.CharField(max_length=4, default='')
    time= models.CharField(max_length=2, default='')
    patient = models.ForeignKey(Patient, null=True,   on_delete=models.CASCADE,)
    doctor = models.ForeignKey(Doctor, null=True,   on_delete=models.CASCADE,)

    def getPatient(self, appoint):
        return appoint.patient



    def getDoctor(self, appoint):
        return appoint.doctor
