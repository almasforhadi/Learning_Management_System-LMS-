# lms/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('enroll/<int:course_id>/', EnrollCourseView.as_view()),
    path('dashboard/admin/', AdminDashboardView.as_view()),
    path('dashboard/instructor/', InstructorDashboardView.as_view()),
    path('dashboard/student/', StudentDashboardView.as_view()),
    path("my-courses/", MyCoursesView.as_view()),
]
