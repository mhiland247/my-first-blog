import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=254)
    birth_date = models.DateField()

    def __str__(self):
        return self.first_name

    def __str__(self):
        return self.last_name

    def __str__(self):
        return self.email_address

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    def _get_full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)

class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(max_length=2,
                                      choices=YEAR_IN_SCHOOL_CHOICES,
                                      default=FRESHMAN)

class Gender(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    TRANSGENDER = 'T'
    GENDER_TYPE_CHOICES = (
	(MALE, 'Male'),
	(FEMALE, 'Female'),
	(TRANSGENDER, 'Transgender'),
    )
    gender_type = models.CharField(max_length=1,
                                      choices=GENDER_TYPE_CHOICES,
                                      default=MALE)
				
