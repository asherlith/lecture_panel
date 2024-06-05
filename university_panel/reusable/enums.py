from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class Weekday(IntegerChoices):
    mon = 0, _('دوشنبه')
    tue = 1, _('سه شنبه')
    wed = 2, _(' چهارشنبه شنبه')
    thu = 3, _('دوشنبه')
    fri = 4, _('دوشنبه')
    sat = 5, _('دوشنبه')
    sun = 6, _('دوشنبه')