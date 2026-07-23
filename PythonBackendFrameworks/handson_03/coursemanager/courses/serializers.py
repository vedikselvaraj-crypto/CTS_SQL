"""
================================================================================
DRF SERIALIZERS (courses/serializers.py)
================================================================================
Translates Django ORM model instances into native Python primitives for JSON 
serialization and handles incoming deserialization validation.
================================================================================
"""

from rest_framework import serializers
from courses.models import Department, Course, Student, Enrollment


class DepartmentSerializer(serializers.ModelSerializer):
    """Serializer for Department model."""
    class Meta:
        model = Department
        fields = ['id', 'name', 'head_of_dept', 'budget']


class CourseSerializer(serializers.ModelSerializer):
    """Serializer for Course model."""
    department_name = serializers.ReadOnlyField(source='department.name')

    class Meta:
        model = Course
        fields = ['id', 'name', 'code', 'credits', 'department', 'department_name']

    def validate_credits(self, value: int) -> int:
        """Field-level validation for course credits."""
        if value <= 0 or value > 10:
            raise serializers.ValidationError("Course credits must be between 1 and 10.")
        return value


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for Student model."""
    department_name = serializers.ReadOnlyField(source='department.name')

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'department', 'department_name', 'enrollment_year']


class EnrollmentSerializer(serializers.ModelSerializer):
    """Serializer for Enrollment model."""
    student_name = serializers.ReadOnlyField(source='student.email')
    course_code = serializers.ReadOnlyField(source='course.code')

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'student_name', 'course', 'course_code', 'enrollment_date', 'grade']
