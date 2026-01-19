from django.db import models
from django.contrib.auth.models import AbstractUser

# accounts/models.py

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin','Admin'),
        ('student','Student'),
        ('instructor','Instructor')
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='student')

    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    student_id = models.CharField(max_length=50, blank=True)
    instructor_experience = models.PositiveIntegerField(null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = 'admin'   # 🔥 superuser হলে role automatically admin হবে
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} - {self.role}"







"""1️⃣ User model-এ শুধু role কেন নিলাম ?

কারণ তুমি AbstractUser ব্যবহার করছো।
AbstractUser আগে থেকেই এগুলো দেয়:

username, email, password, first_name, last_name ইত্যাদি

তাই এগুলো আবার লিখতে হয় না।
তুমি যেটা নতুন যোগ করতে চাও শুধু সেটাই লিখেছো → role  



2️⃣ email, password model-এ না লিখে serializer-এ কেন নিলাম?

Model = ডাটাবেসে কী থাকবে
Serializer = API দিয়ে কী আসবে/যাবে

email, password আগেই User model-এ আছে,
তাই model-এ নতুন করে লিখতে হয়নি।
কিন্তু API থেকে এগুলো নেওয়ার জন্য serializer-এ দিতে হয়েছে।



🔹**************** USERNAME_FIELD = 'username'  ***************

👉 Django-কে বলে login করার সময় কোন field main হবে
এখানে → username

🔹 REQUIRED_FIELDS = ['email']

👉 Django-কে বলে user create করতে email অবশ্যই লাগবে

❌ এটা না থাকলে
→ email database-এ required হলেও
→ Django জানত না
→ তাই 400 Bad Request আসছিল

✅ এটা দেওয়ার পর
→ Django + Serializer + DB sync
→ Registration ঠিকমতো কাজ করছে
"""