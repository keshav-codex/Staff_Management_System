from django.contrib import admin
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display =('name', 'email', 'phone', 'department', 'designation', 'joining_date', 'salary', 'created_at')
    search_fields =('name', 'email', 'phone', 'department', 'designation')
    list_filter =('department', 'designation', 'joining_date')
    ordering =('id',)