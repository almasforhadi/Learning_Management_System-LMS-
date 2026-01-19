# lms/views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdmin, IsInstructor, IsStudent
from .models import Course, CourseCategory, Enrollment
from rest_framework.response import Response
from accounts.models import User
from .serializers import *
from rest_framework.permissions import SAFE_METHODS

# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        # POST, PUT, DELETE → Only Admin
        return [IsAuthenticated(), IsAdmin()]




class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'admin':
            return Course.objects.all()
        elif user.role == 'instructor':
            return Course.objects.filter(instructor=user)
        else:
            return Course.objects.filter(is_active=True)

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)





class EnrollCourseView(APIView):
    permission_classes = [IsAuthenticated, IsStudent]

    def post(self, request, course_id):
        Enrollment.objects.get_or_create(
            student=request.user,
            course_id=course_id
        )
        return Response({"message": "Enrolled successfully"})



class AdminDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({
            "total_users": User.objects.count(),
            "students": User.objects.filter(role='student').count(),
            "instructors": User.objects.filter(role='instructor').count(),
            "total_courses": Course.objects.count(),
            "total_enrollments": Enrollment.objects.count(),
        })


class InstructorDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsInstructor]

    def get(self, request):
        courses = Course.objects.filter(instructor=request.user)
        enrollments = Enrollment.objects.filter(course__in=courses)

        return Response({
            "my_courses": courses.count(),
            "total_students": enrollments.count(),
        })


class StudentDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsStudent]

    def get(self, request):
        enrolled = Enrollment.objects.filter(student=request.user)
        return Response({
            "enrolled_courses": enrolled.count()
        })


class MyCoursesView(APIView):
    permission_classes = [IsAuthenticated, IsStudent]

    def get(self, request):
        enrollments = Enrollment.objects.filter(student=request.user)
        courses = Course.objects.filter(
            id__in=enrollments.values_list('course_id', flat=True)
        )

        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
