from django.contrib import admin
from .models import *


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    ...


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    ...


@admin.register(StudyField)
class StudyFieldAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)


