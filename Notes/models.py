from argparse import _MutuallyExclusiveGroup
from tkinter import CASCADE
from urllib import request
from django.db import models

# Create your models here.


class Stream(models.Model):
    Stream_id = models.CharField(primary_key=True, max_length=10)
    Stream_name = models.CharField(max_length=50)
    Total_Sem = models.IntegerField()
    Total_year = models.IntegerField()


class Subject(models.Model):
    Sub_id = models.CharField(primary_key=True, max_length=10)
    Stream_id = models.ForeignKey('Stream', on_delete=models.CASCADE)
    Sub_name = models.CharField(max_length=100)


class Topic(models.Model):
    Topic_id = models.CharField(primary_key=True, max_length=10)
    Sub_id = models.ForeignKey('Subject', on_delete=models.CASCADE)
    Topic_name = models.CharField(max_length=100)

class College(models.Model):
    College_id = models.IntegerField(primary_key=True)
    College_name = models.CharField(max_length=200)    

class Student(models.Model):
    Student_Email = models.CharField(primary_key=True,max_length=50)
    Student_Phone = models.IntegerField()
    Student_Name = models.CharField(max_length=100)
    Student_College_id = models.ForeignKey('College',on_delete=models.CASCADE)
    Student_Stream_id = models.ForeignKey('Stream', on_delete=models.CASCADE)
    Student_Year_OF_PAASING = models.IntegerField()
    Student_Password = models.CharField(max_length=100)


class Teacher(models.Model):
    Teacher_Email = models.CharField(primary_key=True,max_length=40)
    Teacher_Phone = models.IntegerField()
    Teacher_Name = models.CharField(max_length=100)
    College_id = models.ForeignKey('College',on_delete=models.CASCADE)
    Stream_id = models.ForeignKey('Stream', on_delete=models.CASCADE)
    Teacher_Password = models.CharField(max_length=100)

class Notes(models.Model):
    Notes_id = models.IntegerField()
    Name = models.CharField(max_length=100)
    Stream_id =  models.ForeignKey('Stream', on_delete=models.CASCADE)
    Sub_id = models.ForeignKey('Subject', on_delete=models.CASCADE)
    # path = 
    Teacher_Email = models.ForeignKey('Teacher',on_delete=models.CASCADE)
    Approved = models.BooleanField()  
