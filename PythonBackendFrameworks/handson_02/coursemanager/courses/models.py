"""
================================================================================
DJANGO DATA MODELS (courses/models.py)
================================================================================
Defines database entities, fields, relationships, constraints, and string representations
for the Course Management System.
================================================================================
"""

from django.db import models


class Department(models.Model):
    """Represents an academic department within the college."""
    name = models.CharField(max_length=100, unique=True, help_text="Department name")
    head_of_dept = models.CharField(max_length=100, help_text="Department Head/Chairperson")
    budget = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, help_text="Annual department budget")

    class Meta:
        ordering = ['name']
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self) -> str:
        return f"{self.name} (Head: {self.head_of_dept})"


class Course(models.Model):
    """Represents an academic course offered by a department."""
    name = models.CharField(max_length=150, help_text="Course title")
    code = models.CharField(max_length=20, unique=True, help_text="Unique course code (e.g. CS-101)")
    credits = models.PositiveIntegerField(default=3, help_text="Credit points")
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='courses',
        help_text="Department offering this course"
    )

    class Meta:
        ordering = ['code']
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"


class Student(models.Model):
    """Represents a student enrolled in the college."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, help_text="Student unique email address")
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='students',
        help_text="Major department"
    )
    enrollment_year = models.PositiveIntegerField(default=2026, help_text="Year of admission")

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.email})"


class Enrollment(models.Model):
    """Junction table managing Student to Course enrollment mappings."""
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    enrollment_date = models.DateField(auto_now_add=True, help_text="Date student enrolled")
    grade = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        help_text="Course letter grade (e.g. A, B+, C)"
    )

    class Meta:
        unique_together = [['student', 'course']]
        ordering = ['-enrollment_date']
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"

    def __str__(self) -> str:
        return f"{self.student.first_name} {self.student.last_name} -> {self.course.code}"
