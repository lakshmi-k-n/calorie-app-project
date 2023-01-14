from django.db import models
from utilities.models import TimestampedModel
from django.conf import settings
from django.db.models import JSONField
# from datetime import datetime
from django.utils import timezone


class FoodItem(TimestampedModel):
    name = models.CharField(max_length=150)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="food_items",
                             on_delete=models.CASCADE)
    calories = models.IntegerField(default=0)
    macros = JSONField(default=dict)
    is_global = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)


class Activity(TimestampedModel):
    name = models.CharField(max_length=150)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="activities",
                             on_delete=models.CASCADE)
    calories_burnt = models.IntegerField(default=0)
    is_global = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)