from django.contrib import admin
from .models import *


class StudentLectureInline(admin.TabularInline):
    model = StudentLecture
    extra = 0


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    ...


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = (StudentLectureInline,)


@admin.register(StudyField)
class StudyFieldAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
