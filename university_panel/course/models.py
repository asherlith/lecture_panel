from django.db import models

from user.models import Profile


class Course(models.Model):
    name = models.CharField(max_length=30)
    prerequisite = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='pre_courses'
    )
    corequisite = models.ForeignKey(
        'Course',
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
    semester = models.ManyToManyField(through='SemesterLecture', to='Semester')


class Student(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='student')
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    study_field = models.ForeignKey(
        StudyField,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='students'
    )
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    semesters = models.ManyToManyField(through='StudentSemester', to='Semester')
    lectures = models.ManyToManyField(through='StudentLecture', to='Lecture')


class SemesterLecture(models.Model):
    semester = models.ForeignKey(
        'Semester',
        on_delete=models.CASCADE,
        related_name='semester'

    )
    lecture = models.ForeignKey(
        'Lecture',
        on_delete=models.CASCADE,
        related_name='lecture'
    )


class Semester(models.Model):
    title = models.CharField(max_length=100)


class StudentSemester(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='student_semester'
    )
    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE,
        related_name='student_lecture'
    )


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
    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE,
        related_name='semesters'
    )
