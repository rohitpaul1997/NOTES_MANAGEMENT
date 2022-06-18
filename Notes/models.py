from argparse import _MutuallyExclusiveGroup
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


class Student(models.Model):
    Roll = models.IntegerField(primary_key=True)
    Email = models.CharField(max_length=50)
    Phone = models.IntegerField()
    Name = models.CharField(max_length=100)
    College = models.CharField(max_length=100)
    Stream_id = models.ForeignKey('Stream', on_delete=models.CASCADE)
    Year_OF_PAASING = models.IntegerField()
    Password = models.CharField(max_length=100)


class Teacher(models.Model):
    Emp_id = models.CharField(primary_key=True, max_length=30)
    Email = models.CharField(max_length=50)
    Phone = models.IntegerField()
    Name = models.CharField(max_length=100)
    Stream_id = models.ForeignKey('Stream', on_delete=models.CASCADE)
    Password = models.CharField(max_length=100)
