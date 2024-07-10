from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Lecture, Lecturer, Course, StudentLecture
from reusable.enums import LectureEnum
from .serializers import LectureSerializer, InputLectureSerializer, CourseSerializer, \
    LecturerSerializer


class LectureView(APIView):
    serializer_class = InputLectureSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return Response(
            data=LectureSerializer(Lecture.objects.all(), many=True).data
        )

    def post(self, request, *args, **kwargs):
        if not request.user.profiles.last().is_student:
            lecture = InputLectureSerializer(data=request.data)
            if lecture.is_valid() and not Lecture.objects.filter(
                    day=lecture.validated_data.get('day'),
                    times=lecture.validated_data.get('times'),
                    lecturer=lecture.validated_data.get('lecturer'),

            ).exists():
                lecture = lecture.save()
                return Response(
                    data=self.serializer_class(lecture).data
                )
            return Response(
                status=status.HTTP_406_NOT_ACCEPTABLE,
                data={'data': 'اطلاعات به درستی وارد نشده است.'}
            )
        return Response(
            status=status.HTTP_403_FORBIDDEN,
            data={'data': 'مجاز به انجام این عمل نمی باشید.'}
        )


class DetailLectureView(APIView):
    serializer_class = LectureSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return Response(
            data=self.serializer_class(
                Lecture.objects.filter(pk=kwargs.get('pk')).first()).data

        )

    def delete(self, request, *args, **kwargs):
        if not request.user.profiles.last().is_student:

            try:
                Lecture.objects.filter(pk=kwargs.get('pk')).first().delete()

                return Response(
                    status=status.HTTP_200_OK,
                    data={'data': 'درس با موفقیت حذف گشت.'})

            except:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={'data': 'حذف درس موفقیت آمیز نبود.'})

        return Response(
            status=status.HTTP_403_FORBIDDEN,
            data={'data': 'مجاز به انجام این عمل نمی باشید.'}
        )


class LecturerView(APIView):
    serializer_class = LecturerSerializer

    def get(self, request, *args, **kwargs):
        return Response(
            data=self.serializer_class(
                Lecturer.objects.all(),
                many=True
            ).data
        )


class CourseView(APIView):
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        return Response(
            data=self.serializer_class(
                Course.objects.all(),
                many=True).data
        )


class StudentLectureView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        profile = request.user.profiles.last()

        if profile.is_student:
            student = profile.student.last()
            stu_lec = StudentLecture.objects.filter(student=student)
            lectures = [lec.lecture for lec in stu_lec]
            return Response(LectureSerializer(lectures, many=True).data)

        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'data': 'مجاز به این عمل نیستید.'})

    def post(self, request, *args, **kwargs):
        profile = request.user.profiles.last()

        if profile.is_student:
            student = profile.student.last()
            lecture_id = request.data.get('lecture_id')
            if StudentLecture.objects.filter(student=student, lecture_id=lecture_id):
                return Response(
                    status=status.HTTP_403_FORBIDDEN,
                    data={'data': 'مجاز به اخذ این درس نیستید.'}
                )
            else:
                StudentLecture.objects.create(student=student, lecture_id=lecture_id, status=LectureEnum.NO_STATUS)

                return Response(
                    status=status.HTTP_200_OK,
                    data={'data': 'درس ثبت گشت.'}
                )


class StudentDetailLectureView(APIView):
    def delete(self, request, *args, **kwargs):
        profile = request.user.profiles.last()

        if profile.is_student:
            student = profile.student.last()
            lecture_id = kwargs.get('pk')

            lec = StudentLecture.objects.filter(
                student=student,
                lecture_id=lecture_id,
                status=LectureEnum.NO_STATUS
            ).last()

            if lec:
                lec.delete()
                return Response(
                    status=status.HTTP_200_OK,
                    data={'data': 'با موفقیت حذف گشت.'}
                )
            else:
                return Response(
                    status=status.HTTP_403_FORBIDDEN,
                    data={'data': 'مجاز به انجام این عمل نیستید.'}
                )
