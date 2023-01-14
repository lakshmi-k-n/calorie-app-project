from django.db import models
from django.contrib.auth.models import AbstractUser
from food.models import FoodItem, Activity
from utilities.models import TimestampedModel
from django.conf import settings
# from datetime import datetime
from django.utils import timezone
# Create your models here.


class CustomUser(AbstractUser):
    # in cm 
    height = models.IntegerField(default=0)
    # in kg
    weight = models.IntegerField(default=0)
    age = models.IntegerField(default=0)


class MealLog(TimestampedModel):
    food_item = models.ForeignKey(FoodItem,
                             related_name="meal_logs",
                             on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="meal_logs",
                             on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)
    total_calories_consumed = models.IntegerField(default=0)


class ActivityLog(TimestampedModel):
    activity = models.ForeignKey(Activity,
                             related_name="activity_logs",
                             on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="activity_logs",
                             on_delete=models.CASCADE)
    duration = models.IntegerField(default=0)
    calories_burnt = models.IntegerField(default=0)