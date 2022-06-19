from argparse import _MutuallyExclusiveGroup
from tkinter import CASCADE
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
    College_id = models.CharField(primary_key=True, max_length=10)
    College_name = models.CharField(max_length=200)    

class Student(models.Model):
    Email = models.CharField(primary_key=True,max_length=50)
    Phone = models.IntegerField()
    Name = models.CharField(max_length=100)
    College_id = models.ForeignKey('College',on_delete=models.CASCADE)
    Stream_id = models.ForeignKey('Stream', on_delete=models.CASCADE)
    Year_OF_PAASING = models.IntegerField()
    Password = models.CharField(max_length=100)


class Teacher(models.Model):
    Email = models.CharField(max_length=50)
    Phone = models.IntegerField()
    Name = models.CharField(max_length=100)
    College_id = models.ForeignKey('College',on_delete=models.CASCADE)
    Stream_id = models.ForeignKey('Stream', on_delete=models.CASCADE)
    Password = models.CharField(max_length=100)
