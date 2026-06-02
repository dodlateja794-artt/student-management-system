from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    photo=models.ImageField(upload_to='students/',blank=True,null=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(1), MaxValueValidator(100)])
    course=models.CharField(max_length=50)
    marks=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)])
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


