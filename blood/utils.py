from enum import IntEnum
from django.utils.translation import gettext_lazy as _
from django.db import models


class DonationStatus(IntEnum):
    RUNNING = 0
    FINISHED = 1

    @classmethod
    def get_choices(cls):
        return [(key.value, key.name) for key in cls]


class SelectGender(IntEnum):
    OTHERS= 0
    MALE= 1
    FEMALE = 2
    
    @classmethod
    def select_gender(cls):
        return [(key.value, key.name) for key in cls]


class BloodGroup(models.TextChoices):
    AB = 'AB', _('AB posation')
    ABN = 'AB-', _('AB Negative')
    BP = 'B+', _('B Positive')
    BN = 'B-', _('B Negative')
    AP = 'A+', _('A Positive')
    AN = 'A-', _('A Negative')
    OP = 'O+', _('O Posative')
    ON = 'O-', _('O Negative')
