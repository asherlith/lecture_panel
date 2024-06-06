from rest_framework import serializers

from course.models import Lecture, Course, Lecturer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'name',
            'prerequisite',
            'corequisite',
        )


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = (
            'name',
            'last_name',
            'phone',
            'email'
        )


class InputLectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = (
            'title',
            'times',
            'course',
            'lecturer',
            'credits_count',
        )


class LectureSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Lecture
        fields = (
            'title',
            'times',
            'course',
            'lecturer',
            'credits_count',

        )

