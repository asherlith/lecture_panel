from enum import Enum

from django.db import models
from django.db.models import TextChoices

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


class StudyField(models.Model):
    title = models.CharField(max_length=50)


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


class Lecture(models.Model):
    title = models.CharField(max_length=30)
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


class LectureEnum(TextChoices):
    PASS = 'pass', 'پاس'
    FAIL = 'fail', 'رد'
    NO_STATUS = 'no status', 'داده خالی'


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
