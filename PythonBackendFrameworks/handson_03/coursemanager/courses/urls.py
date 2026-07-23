"""
================================================================================
DRF URL ROUTER & PATHS (courses/urls.py)
================================================================================
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses.views import (
    CourseListView,
    CourseDetailView,
    DepartmentViewSet,
    CourseViewSet,
    StudentViewSet,
    EnrollmentViewSet
)

# Instantiate DefaultRouter for automatic ViewSet URL generation
router = DefaultRouter()
router.register('departments', DepartmentViewSet, basename='department')
router.register('courses', CourseViewSet, basename='course')
router.register('students', StudentViewSet, basename='student')
router.register('enrollments', EnrollmentViewSet, basename='enrollment')

urlpatterns = [
    # Explicit APIView Endpoint Paths
    path('apiview/courses/', CourseListView.as_view(), name='apiview_course_list'),
    path('apiview/courses/<int:pk>/', CourseDetailView.as_view(), name='apiview_course_detail'),

    # Include DRF Router generated URLs
    path('', include(router.urls)),
]
