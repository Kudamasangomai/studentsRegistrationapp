from uuid import uuid4
from django.db import models
import random
from datetime import datetime



def random_reg_number():
    return str(random.randint(1001,9999))



class students(models.Model):

    sex_choices =(
        ('Male','Male'),
        ('Female','Female')
    )
    
    student_firstname = models.CharField(max_length=20)
    student_lastname = models.CharField(max_length=20)
    student_email = models.CharField(max_length=255,unique=True)
    student_regnumber = models.CharField(max_length=20,default=random_reg_number)
    student_sex = models.CharField(max_length=6,choices=sex_choices,default=sex_choices)
    date_created = models.DateTimeField(default=datetime.today) 

    def _str__(self):
        return self.student_firstname
    
    class Meta:
    		ordering = ['-date_created']

class votes(models.Model):
    uid = models.UUIDField(max_length=10,default=uuid4)
    studentid = models.CharField(max_length=5)
    upvoted = models.CharField(max_length=3)

    def __str__(self):
        return self.studentid
