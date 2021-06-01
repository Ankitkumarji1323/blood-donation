from django.db import models

from blood.models.base import DomainEntity


class Campaign(DomainEntity):
    campaign_name = models.CharField(max_length=120)
    day_name = models.CharField(max_length=35)
    sponsor_by = models.CharField(max_length=150, blank=True, null=True)
    location = models.CharField(max_length=200)
    material_cost = models.IntegerField(default=0)
    other_cost = models.IntegerField(default=0)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.campaign_name[:30]

    def _total_cost(self):
        return f"Total cost: {self.material_cost + self.other_cost}"
