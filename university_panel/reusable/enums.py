from django.db.models import TextChoices


class LectureEnum(TextChoices):
    PASS = 'pass', 'پاس'
    FAIL = 'fail', 'رد'
    NO_STATUS = 'no status', 'داده خالی'
