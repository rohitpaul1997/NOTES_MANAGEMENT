from itertools import count
from multiprocessing import context
import string
from django.db.models import Max
from django import db
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import College, Stream, Student, Teacher
from django.core import serializers
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
import django.contrib.messages as messages
import django.contrib.sessions as session
from django.core.files.storage import FileSystemStorage

# Create your views here.


def home(request):
    return render(request, 'Home.html')


def signup_Student(request):
    if(request.method == 'POST'):
        Email = request.POST['Email']
        Name = request.POST['Name']
        Phone = request.POST['Phone']
        Password = request.POST['Password']
        RPassword = request.POST["RPassword"]
        encryptedpassword = make_password(Password)
        checkpassword = check_password(RPassword, encryptedpassword)
        CCollege = request.POST['college']
        Year = request.POST['Year']
        stream = request.POST['Stream']
        if checkpassword:
            obj = Student(Email, Phone, Name, CCollege,
                          stream, Year, encryptedpassword)
            # subject = 'welcome To My App'
            # message = "Hi"
            # email_from = settings.EMAIL_HOST_USER
            # print(email_from)
            # recipient_list = [Email, ]
            # print(recipient_list)
            # send_mail( subject, message, email_from, recipient_list )
            obj.save()
            print(stream, encryptedpassword)
            return render(request, 'Home.html')
        else:
            print("Hoeni")
    else:
        record = Stream.objects.filter().only('Stream_id', 'Stream_name')
        college = College.objects.filter().only('College_id', 'College_name')
        context = {
            'record': record,
            'college': college,
        }
        return render(request, 'Register.html', context)


def signup_Teacher(request):
    if(request.method == 'POST'):
        Email = request.POST['Email']
        Name = request.POST['Name']
        Phone = request.POST['Phone']
        Password = request.POST['Password']
        RPassword = request.POST["RPassword"]
        encryptedpassword = make_password(Password)
        checkpassword = check_password(RPassword, encryptedpassword)
        CCollege = request.POST['college']
        stream = request.POST['Stream']
        if checkpassword:
            obj = Teacher(Email, Phone, Name, CCollege,
                          stream, encryptedpassword)
            # subject = 'welcome To My App'
            # message = "Hi"
            # email_from = settings.EMAIL_HOST_USER
            # print(email_from)
            # recipient_list = [Email, ]
            # print(recipient_list)
            # send_mail( subject, message, email_from, recipient_list )
            obj.save()
            # print(stream,encryptedpassword)
            return render(request, 'Home.html')
        else:
            print("Hoeni")
    else:
        record = Stream.objects.filter().only('Stream_id', 'Stream_name')
        college = College.objects.filter().only('College_id', 'College_name')
        context = {
            'record': record,
            'college': college,
        }
        return render(request, 'Register_Mentor.html', context)


def AddCollege(request):
    if(request.method == 'POST'):
        College_name = request.POST['College']
        College_id = 1 if(College.objects.count() == 0) else College.objects.aggregate(
            max=Max('College_id'))["max"]+1
        db.connections.close_all()
        obj = College(College_id, College_name)
        obj.save()
        return render(request, 'Home.html')
    else:
        return render(request, 'Add_College.html')


def login(request):
    if(request.method == 'POST'):
        email = request.POST['Email']
        ppassword = request.POST['lpassword']
        loginAs = request.POST['As']
        if loginAs == 'Student':
            st = Student.objects.filter(Email=email).only('Password')
            if not st:
                messages.error(request, 'Please enter a corect email')
                # print("Incorrect email")
            else:
                dpass = ''
                for i in st:
                    dpass = i.Password
                    # print(dpass)
                checkpassword = check_password(ppassword, dpass)
                if checkpassword:
                    request.session['u_email'] = email
                    return redirect('/dashboard/')
                else:
                    messages.error(
                        request, 'Please enter a corect password')
            # return render(request, 'Login.html', context)
        elif loginAs == 'Mentor':
            mn = Teacher.objects.filter(Email=email).only('Password')
            if not mn:
                messages.error(request, 'Please enter a corect email')
                # print("Incorrect email")
            else:
                dpass = ''
                for i in mn:
                    dpass = i.Password
                    # print(dpass)
                checkpassword = check_password(ppassword, dpass)
                if checkpassword:
                    request.session['u_email'] = email
                    return redirect('/dashboard/')
                else:
                    messages.error(
                        request, 'Please enter a corect password')
            # return render(request, 'Login.html')
    else:
        return render(request, 'Login.html')


def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return redirect('/')


def dashboard(request):
    # print(request.session['u_email'])
    return render(request, 'dashboard.html')


def addnotes(request):
    pass
