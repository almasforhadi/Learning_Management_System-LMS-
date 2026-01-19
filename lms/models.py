from django.db import models
from accounts.models import User

# Create your models here.

class CourseCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    category = models.ForeignKey(CourseCategory,on_delete=models.CASCADE,null=True)
    instructor = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'role':'instructor'})
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class Enrollment(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'role':'student'})
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} -> {self.course}"