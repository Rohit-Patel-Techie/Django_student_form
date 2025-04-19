from django.db import models
from django.utils import timezone

GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
STATUS_CHOICES = [('Single', 'Single'), ('Married', 'Married')]

class Student(models.Model):
   
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    
    present_address = models.TextField()
    
    nationality = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    occupation = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    course_name = models.CharField(max_length=100)
    
    photo = models.ImageField(upload_to='photos/')
    signature = models.ImageField(upload_to='signatures/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.student_name