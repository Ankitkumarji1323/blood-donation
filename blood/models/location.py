from django.db import models
from blood.models.base import DomainEntity


class Location(DomainEntity):
    name = models.CharField(max_length=95)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
