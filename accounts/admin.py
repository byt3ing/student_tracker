
from django.contrib import admin
from .models import Student, ExamRegistration

# Simple registration (just to make them appear)
admin.site.register(Student)
admin.site.register(ExamRegistration)