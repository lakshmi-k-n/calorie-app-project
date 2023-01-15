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
    #Calories contained in 100g of food item
    calories = models.IntegerField(default=0)
    # Store macros as a dict in %
    # eg. {'carbs': 10,'fat': 30,'protein': 70}
    macros = JSONField(default=dict)
    is_global = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


class Activity(TimestampedModel):
    name = models.CharField(max_length=150)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="activities",
                             on_delete=models.CASCADE)
    #Calories burnt in 30 minutes
    calories_burnt = models.IntegerField(default=0)
    is_global = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)