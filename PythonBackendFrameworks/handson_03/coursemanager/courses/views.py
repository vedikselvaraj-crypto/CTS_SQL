"""
================================================================================
DRF API VIEWS AND VIEWSETS (courses/views.py)
================================================================================
Implements APIView class-based views, ModelViewSets, and custom detail actions.
================================================================================
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from courses.models import Department, Course, Student, Enrollment
from courses.serializers import (
    DepartmentSerializer,
    CourseSerializer,
    StudentSerializer,
    EnrollmentSerializer
)


# ==============================================================================
# TASK 1: APIVIEW CLASS-BASED VIEWS
# ==============================================================================

class CourseListView(APIView):
    """APIView handling collection requests: GET list and POST create."""

    def get(self, request) -> Response:
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(APIView):
    """APIView handling individual resource operations: GET, PUT, DELETE."""

    def get(self, request, pk: int) -> Response:
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk: int) -> Response:
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int) -> Response:
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ==============================================================================
# TASK 2: MODELVIEWSETS AND CUSTOM ACTIONS
# ==============================================================================

class CourseViewSet(viewsets.ModelViewSet):
    """ModelViewSet providing full 5 CRUD operations automatically for Course."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'], url_path='students')
    def students(self, request, pk=None) -> Response:
        """Custom Action: GET /api/courses/{id}/students/
        Returns all students currently enrolled in the specified course.
        """
        course = self.get_object()
        enrollments = Enrollment.objects.filter(course=course).select_related('student')
        students = [enrollment.student for enrollment in enrollments]
        
        serializer = StudentSerializer(students, many=True)
        return Response({
            "course_id": course.id,
            "course_code": course.code,
            "total_enrolled_students": len(students),
            "students": serializer.data
        }, status=status.HTTP_200_OK)


class DepartmentViewSet(viewsets.ModelViewSet):
    """ModelViewSet for Department model."""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """ModelViewSet for Student model."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    """ModelViewSet for Enrollment model."""
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
