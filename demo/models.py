from django.db import models
from ext.models import DayIntervalField, EnumField, IntegerArrayField, MoneyField, PointField

class Map(models.Model):
    name = models.CharField(max_length=255)
    geocode = PointField()

class Lotto(models.Model):
    name = models.CharField(max_length=255)
    numbers = IntegerArrayField(blank=True, null=True)

class Subscription(models.Model):
    name = models.CharField(max_length=255)
    period = DayIntervalField()
    price = MoneyField(blank=True, null=True)