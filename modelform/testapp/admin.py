from django.contrib import admin
from testapp.models import student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','rollno','marks']
admin.site.register(student,StudentAdmin)
