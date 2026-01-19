from rest_framework import serializers
from .models import Course, CourseCategory, Enrollment


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    instructor_name = serializers.CharField(
        source='instructor.username',
        read_only=True
    )

    instructor = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = Course
        fields = '__all__'




class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
