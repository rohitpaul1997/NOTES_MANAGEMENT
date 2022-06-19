from multiprocessing import context
from django.conf import settings
from django.shortcuts import render
from .models import Stream, Student, Teacher
from django.core import serializers
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request,'Home.html')

def signup_Student(request):
    if(request.method=='POST'):
        Roll = request.POST['Roll']
        Email = request.POST['Email']
        Name = request.POST['Name']
        Phone = request.POST['Phone']
        Password = request.POST['Password']
        RPassword = request.POST["RPassword"]
        encryptedpassword=make_password(Password)
        checkpassword=check_password(RPassword, encryptedpassword)
        College = request.POST['College'] 
        Year = request.POST['Year']
        stream = request.POST['Stream']
        if checkpassword:
            obj = Student(Roll,Email,Phone,Name,College,stream,Year,encryptedpassword)
            # subject = 'welcome To My App'
            # message = "Hi"
            # email_from = settings.EMAIL_HOST_USER
            # print(email_from)
            # recipient_list = [Email, ]
            # print(recipient_list)
            # send_mail( subject, message, email_from, recipient_list )
            obj.save()
            print(stream,encryptedpassword)
            return render(request,'Home.html')
        else:
            print("Hoeni")      
    else:
        record = Stream.objects.filter().only('Stream_id','Stream_name')
        context={
            'record':record,
        }
        return render(request,'Register.html',context) 

def signup_Teacher(request):
    if(request.method=='POST'):
        Email = request.POST['Email']
        Name = request.POST['Name']
        Phone = request.POST['Phone']
        Password = request.POST['Password']
        RPassword = request.POST["RPassword"]
        encryptedpassword=make_password(Password)
        checkpassword=check_password(RPassword, encryptedpassword)
        College = request.POST['College'] 
        stream = request.POST['Stream']
        if checkpassword:
            obj = Teacher(Email,Phone,Name,College,stream,encryptedpassword)
            # subject = 'welcome To My App'
            # message = "Hi"
            # email_from = settings.EMAIL_HOST_USER
            # print(email_from)
            # recipient_list = [Email, ]
            # print(recipient_list)
            # send_mail( subject, message, email_from, recipient_list )
            obj.save()
            print(stream,encryptedpassword)
            return render(request,'Home.html')
        else:
            print("Hoeni")      
    else:
        record = Stream.objects.filter().only('Stream_id','Stream_name')
        context={
            'record':record,
        }
        return render(request,'Register.html',context)         
          