from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Lecture, Lecturer, Course, StudentLecture, LectureEnum
from .serializers import LectureSerializer, InputLectureSerializer, CourseSerializer, \
    LecturerSerializer


# Create your views here.

class LectureView(APIView):
    serializer_class = InputLectureSerializer

    def get(self, request, *args, **kwargs):
        return Response(
            data=LectureSerializer(Lecture.objects.all(), many=True).data
        )

    def post(self, request, *args, **kwargs):
        if not request.user.is_student:
            lecture = InputLectureSerializer(data=request.data)
            if lecture.is_valid():
                lecture = lecture.save()
                return Response(
                    data=self.serializer_class(lecture).data
                )
            return Response(
                status=status.HTTP_406_NOT_ACCEPTABLE,
                data='اطلاعات به درستی وارد نشده است.'
            )
        return Response(
            status=status.HTTP_403_FORBIDDEN,
            data='مجاز به انجام این عمل نمی باشید.'
        )


class DetailLessonView(APIView):
    serializer_class = LectureSerializer

    def get(self, request, *args, **kwargs):
        return Response(
            data=self.serializer_class(
                Lecture.objects.filter(kwargs.get('pk').first())
            )
        )

    def delete(self, request, *args, **kwargs):
        if not request.user.is_student:

            try:
                Lecture.objects.filter(kwargs.get('pk')).first().delete()

                return Response(
                    status=status.HTTP_200_OK,
                    data='درس با موفقیت حذف گشت.')

            except:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data='حذف درس موفقیت آمیز نبود.')

        return Response(
            status=status.HTTP_403_FORBIDDEN,
            data='مجاز به انجام این عمل نمی باشید.'
        )


class LecturerView(APIView):
    serializer_class = LecturerSerializer

    def get(self, request, *args, **kwargs):
        return Response(
            data=self.serializer_class(
                Lecturer.objects.all())
            )


class CourseView(APIView):
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        return Response(
            data=self.serializer_class(
                Course.objects.all())
            )


class StudentDetailLessonsView(APIView):

    # def get(self, request, *args, **kwargs):
    def post(self, request, *args, **kwargs):
        if request.user.is_student:
            student = request.user.profile.student
            lecture_id = request.data.get('lecture_id')
            if StudentLecture.objects.filter(student=student, lecture__pk=lecture_id, status=LectureEnum.PASS):
                return Response(
                    status=status.HTTP_403_FORBIDDEN,
                    data='مجاز به اخذ این درس نیستید.'
                )
            else:
                StudentLecture.objects.create(student=student, lecture__pk=lecture_id, status=LectureEnum.NO_STATUS)

                return Response(
                    status=status.HTTP_403_FORBIDDEN,
                    data='درس ثبت گشت.'
                )

    def delete(self, request, *args, **kwargs):
        if request.user.is_student:
            student = request.user.profile.student
            lecture_id = request.data.get('lecture_id')

            lec = StudentLecture.objects.filter(
                student=student,
                lecture__pk=lecture_id,
                status=LectureEnum.NO_STATUS
            ).last()

            if lec:
                lec.delete()
                return Response(
                    status=status.HTTP_200_OK,
                    data='با موفقیت حذف گشت.'
                )
            else:
                return Response(
                    status=status.HTTP_403_FORBIDDEN,
                    data='مجاز به انجام این عمل نیستید.'
                )



