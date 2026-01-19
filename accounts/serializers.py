from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="Username already exists")]
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="Email already exists")]
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
            role = validated_data['role']
        )
        return user
    



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'role',
            'bio',
            'phone',
            'student_id',
            'instructor_experience'
        ]
        read_only_fields = ['username', 'role']








""" 3️⃣ Serializer-এ শুধু password = serializers.CharField(write_only=True) কেন লিখলাম?

কারণ:

password plain text হিসেবে save করা যায় না
এটা response-এ দেখানো যাবে না
 write_only=True মানে: API থেকে password পাঠানো যাবে ✔ কিন্তু response-এ দেখাবে না ❌

আর:

username, email, role → ModelSerializer নিজে থেকেই বানিয়ে নেয়

কিন্তু password এর জন্য extra control দরকার → তাই আলাদা লিখতে হয় """