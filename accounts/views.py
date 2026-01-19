from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from .serializers import RegistrationSerializer, ProfileSerializer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import User
from .permissions import IsAdmin
from django.core.mail import send_mail
from django.conf import settings



class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]    # JWT auth + role check

    def get(self, request):
        return Response({"message": "Hello Admin"})



class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]    # Allow any user (authenticated or not) to access this view
    authentication_classes = []        # No auth needed for registration



class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user





class ForgetPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"message": "If email exists, reset link sent"}, status=200)

        token = PasswordResetTokenGenerator().make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        reset_link = f"http://localhost:5173/reset-password/{uid}/{token}"

        send_mail(
            subject="Reset your password",
            message=f"Click the link to reset password:\n{reset_link}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
        )

        return Response(
            {"message": "Password reset link sent to email"},
            status=status.HTTP_200_OK
        )



class ResetPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        uid = request.data.get('uid')
        token = request.data.get('token')
        password = request.data.get('password')

        try:
            user_id = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=user_id)
        except Exception:
            return Response({"error": "Invalid uid"}, status=status.HTTP_400_BAD_REQUEST)

        if not PasswordResetTokenGenerator().check_token(user, token):
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(password)
        user.save()
        return Response({"message": "Password reset successful"},status=status.HTTP_200_OK )



# Create your views here.

# class RegisterView(APIView):
#     def post(self, request):
#         serializer = RegistrationSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message':'User registered successfully'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class ProfileView(APIView):
#     permission_classes = [IsAuthenticated]  # Add appropriate permissions as needed

#     def get(self, request):
#         serializer = ProfileSerializer(request.user)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request):
#         serializer = ProfileSerializer(request.user, data = request.data, partial = True)   # partial=True মানে হলো সব required field না পাঠালেও update হবে।
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






""" 
✅ Industry Standard Flow (Real World)
✔️ আসলে কী হয়?

Step 1: Forgot Password
User শুধু email দেয়
Backend:
uid + token generate করে
একটা reset link বানায়
সেই link email এ পাঠায়
📩 Example email link:
http://localhost:5173/reset-password/NA/4x9f3c-xxxxx


Step 2: User email এ click করে
Frontend এর Reset Password page খুলে
URL থেকে automatically:
uid
token
নেয়

Step 3: User শুধু New Password দেয়
Frontend → backend এ পাঠায়
Password reset complete 
User কখনোই uid/token দেখে না

 """

"""
1️⃣ CreateAPIView (Better)
কারণ:
Clean code
DRF standard
JWT project-এর জন্য suitable


2️⃣ APIView + Serializer 
Beginner-friendly
Logic clear বোঝা যায়
Full control (custom validation, email send ইত্যাদি সহজ)

❌ Cons:
Code বেশি
DRF features কম use হয়


2️⃣ ForgotPasswordView কেন APIView-ই থাকুক?
Custom logic (token, email)
No model create/update directly
Generic view এখানে fit না


"""
"""

User clicks "Forgot Password"
   ↓
Enters email
   ↓
Email sent with link
   ↓
User clicks email link
   ↓
Frontend opens:
   /reset-password/:uid/:token
   ↓
User enters new password
   ↓
Backend verifies token
   ↓
Password updated


 """