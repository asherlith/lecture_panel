from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(
        User, related_name='profiles', on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=100)

    is_student = models.BooleanField(default=False)
    national_code = models.CharField(max_length=50, null=True, blank=True)
