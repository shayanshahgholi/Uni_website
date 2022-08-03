from django.db import models


class Days(models.IntegerChoices):
    SATURDAY = 0, 'Saturday'
    SUNDAY = 1, 'Sunday'
    MONDAY = 2, 'Monday'
    THURSDAY = 3, 'Thursday'
    WEDNESDAY = 4, 'Wednesday'
    NOTSET = 5, 'NotSet'


class Course(models.Model):
    department = models.TextField()
    name = models.TextField()
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.TextField()
    start_time = models.TextField()
    end_time = models.TextField()
    first_day = models.IntegerField(default=Days.NOTSET, choices=Days.choices)
    second_day = models.IntegerField(default=Days.NOTSET, choices=Days.choices)

    def __str__(self):
        return self.name
