from django.contrib import admin
from staff.models import Staff
# Register your models here.

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display=['name','mobile','email','address','gender','experience','skills']