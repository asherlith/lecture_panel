from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import transaction

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from course.models import Student
from user.models import Profile


# Create your views here.
class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response(
                status=status.HTTP_406_NOT_ACCEPTABLE,
                data='این کاربر قبلا ثبت نام کرده است.'
            )
        try:
            with transaction.atomic():
                user = User.objects.create_user(
                    username=request.GET.get('username'),
                    password=request.GET.get('password')
                )

                token = Token.objects.create(user=user).last()

                profile = Profile.objects.create(
                    user=user,
                    is_student=True,
                    national_code=request.GET.get('national_code')
                )
                student = Student.objects.create(profile=profile)

            return Response(
                status=status.HTTP_201_CREATED,
                data='کاربر با موفقیت ثبت شد.'
            )

        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=f'ثبت کاربر با خطا {e}مواجه شد. لطفا بعدا تلاش کنید.'
            )


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.GET.get('username')
        password = request.GET.get('password')

        if authenticate(username=username, password=password):
            user = User.objects.filter(username=username, password=password)
            token = Token.objects.filter(user=user).last()

            return Response(
                status=status.HTTP_202_ACCEPTED,
                data=token
            )
        return Response(
            status=status.HTTP_403_FORBIDDEN,
            data='اطلاعات نادرست است.'
        )

