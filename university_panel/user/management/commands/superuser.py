from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):

        # The magic line
        if not User.objects.filter(username= 'asher',
                                email='asher@super.com').exists():
            User.objects.create_user(
                username='asher',
                email='asher@super.com',
                password='asher',
                is_staff=True,
                is_active=True,
                is_superuser=True
            )