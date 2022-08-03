from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class MoreDetail(models.Model):
    Gender =(
        (0, 'M'),
        (1, 'F'),
        (2, 'NotSet')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.IntegerField(choices=Gender, default=2)
    bio = models.TextField()
    avatar = models.ImageField(upload_to = "images/")

class Course(models.Model):
    Days= (
        (0, 'Saturday'),
        (1, 'Sunday'),
        (2, 'Monday'),
        (3, 'Thursday'),
        (4, 'Wednesday'),
        (5, 'Notset'),
    )

    department = models.TextField()
    name = models.TextField()
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = models.IntegerField(choices=Days)
    second_day = models.IntegerField(choices=Days)

    def __str__(self):
        return self.name
