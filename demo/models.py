from django.db import models
from ext.models import DayIntervalField, EnumField, HstoreField, IntegerArrayField, MoneyField, PointField

class Map(models.Model):
    name = models.CharField(max_length=255)
    geocode = PointField()

class Lotto(models.Model):
    name = models.CharField(max_length=255)
    numbers = IntegerArrayField(blank=True, null=True)

class ParameterLog(models.Model):
    params = HstoreField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Subscription(models.Model):
    name = models.CharField(max_length=255)
    period = DayIntervalField()
    price = MoneyField(blank=True, null=True)