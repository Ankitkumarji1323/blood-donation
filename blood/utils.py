from enum import IntEnum


class DonationStatus(IntEnum):
    RUNNING = 0
    FINISHED = 1

    @classmethod
    def get_choices(cls):
        return [(key.value, key.name) for key in cls]
