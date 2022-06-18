from django.contrib import admin

from .models import Stream, Student, Subject, Teacher, Topic

# Register your models here.
admin.site.register(Stream)
admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Student)
admin.site.register(Teacher)
