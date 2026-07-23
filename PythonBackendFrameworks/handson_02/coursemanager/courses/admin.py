"""
================================================================================
DJANGO ADMIN INTERFACE CONFIGURATION (admin.py)
================================================================================
"""

from django.contrib import admin
from courses.models import Department, Course, Student, Enrollment


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'head_of_dept', 'budget']
    search_fields = ['name', 'head_of_dept']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Customized Admin View for Course Model."""
    list_display = ['name', 'code', 'credits', 'department']
    search_fields = ['name', 'code']
    list_filter = ['department']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'department', 'enrollment_year']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['department', 'enrollment_year']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'course', 'enrollment_date', 'grade']
    search_fields = ['student__first_name', 'student__last_name', 'course__code']
    list_filter = ['grade', 'enrollment_date']
