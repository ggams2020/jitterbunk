#Code by Genna Gams based off of tutorial from django https://docs.djangoproject.com/en/2.2/intro/

import datetime

from django.db import models
from django.utils import timezone

# class representing a Bunk model
class Bunk(models.Model):
    from_user = models.ForeignKey('User', on_delete = models.CASCADE, related_name='f')
    to_user = models.ForeignKey('User', on_delete = models.CASCADE, related_name='t')
    time = models.DateTimeField('date bunked')

    def __str__(self):
        #date formatting help from https://pythonguides.com/python-django-format-date/
        formatted_date = self.time.strftime("%m/%d/%y")
        #time formatting help from https://pythonguides.com/python-django-set-timezone/ 
        formatted_time = self.time.strftime("%H:%M")
        return self.to_user.username + " bunked by " + self.from_user.username + " on " + formatted_date + " at " + formatted_time

# class representing a User model
class User(models.Model):
    username = models.CharField(max_length = 100)
    photo = models.CharField(max_length = 100)

    def __str__(self):
        return self.username

