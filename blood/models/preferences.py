from django.db import models

from blood.models.base import DomainEntity


class ApplicationSetting(DomainEntity):
    logo = models.ImageField(upload_to='application', blank=True, null=True)
    favicon = models.ImageField(upload_to='application', blank=True, null=True)
    site_name = models.CharField(max_length=100, default='My site')

    def __str__(self):
        return self.site_name[:30]
