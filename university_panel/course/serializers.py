from rest_framework import serializers

from course.models import Lecture, Course, Lecturer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'prerequisite',
            'corequisite',
        )


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = (
            'id',
            'name',
            'last_name',
            'phone',
            'email'
        )


class InputLectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = (
            'day',
            'times',
            'course',
            'lecturer',
            'credits_count',
        )


class LectureSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    lecturer = LecturerSerializer()

    class Meta:
        model = Lecture
        fields = (
            'id',
            'day',
            'times',
            'course',
            'lecturer',
            'credits_count',
        )

