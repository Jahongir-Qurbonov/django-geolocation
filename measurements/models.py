from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Measurement(models.Model):

    class Meta:
        verbose_name = _('measurement')
        verbose_name_plural = _('measurements')

    location = models.CharField(_('location'), max_length=200)
    destination = models.CharField(_('destionation'), max_length=200)
    distance = models.DecimalField(_('distance'), max_digits=10, decimal_places=2)
    created = models.DateField(_('created'), auto_now_add=True)

    def __str__(self) -> str:
        return f"Distance from {self.location} to {self.destination} is {self.distance} km"
