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
                data={'data': 'این کاربر قبلا ثبت نام کرده است.'}
            )
        try:
            with transaction.atomic():
                user = User.objects.create_user(
                    first_name=request.data.get('first_name'),
                    last_name=request.data.get('last_name'),
                    email=request.data.get('email'),
                    username=request.data.get('username'),
                    password=request.data.get('password')
                )

                token = Token.objects.create(user=user)

                profile = Profile.objects.create(
                    user=user,
                    is_student=True,
                    national_code=request.data.get('national_code')
                )
                student = Student.objects.create(profile=profile)

            return Response(
                status=status.HTTP_201_CREATED,
                data={'data': 'کاربر با موفقیت ثبت شد.' }
            )

        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'data': f'ثبت کاربر با خطا {e}مواجه شد. لطفا بعدا تلاش کنید.'}
            )


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if authenticate(username=username, password=password):
            user = User.objects.filter(username=username).last()
            token = Token.objects.filter(user=user).last()

            if not token:
                token = Token.objects.create(user=user)

            return Response(
                status=status.HTTP_202_ACCEPTED,
                data={'data': str(token)}
            )
        return Response(
            status=status.HTTP_403_FORBIDDEN,
            data={'data': 'اطلاعات نادرست است.'}
        )

