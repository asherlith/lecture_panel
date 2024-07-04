from django.db import models

from reusable.enums import LectureEnum
from user.models import Profile


class Course(models.Model):
    name = models.CharField(max_length=30)
    prerequisite = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='pre_courses'
    )
    corequisite = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='co_courses'
    )

    def __str__(self):
        return self.name


class StudyField(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Lecturer(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    study_field = models.ForeignKey(
        StudyField,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='lecturers'
    )
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Lecture(models.Model):
    times = models.JSONField(default=dict)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lectures'
    )
    lecturer = models.ForeignKey(
        Lecturer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='lectures'

    )
    credits_count = models.IntegerField()
    day = models.CharField(null=True, blank=True, max_length=20)

    def __str__(self):
        return self.title


class Student(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='student')
    study_field = models.ForeignKey(
        StudyField,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='students'
    )
    lectures = models.ManyToManyField(through='StudentLecture', to='Lecture', null=True, blank=True)

    def __str__(self):
        return f'{self.profile.user.first_name} {self.profile.user.last_name}'


class StudentLecture(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='students'
    )
    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE,
        related_name='lectures'
    )
    status = models.CharField(choices=LectureEnum, default=LectureEnum.PASS)

    def __str__(self):
        return f'{self.student.profile.user.first_name} {self.student.profile.user.last_name} --- {self.lecture.title}'
