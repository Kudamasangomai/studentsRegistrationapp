from django.contrib import admin
from .models import students

# Register your models here.
class studentsadmin(admin.ModelAdmin):
    list_display = ('student_firstname','student_lastname','student_email','student_regnumber','student_sex','date_created')
admin.site.register(students,studentsadmin)