from rest_framework import serializers
from food.models import FoodItem, Activity
from users.models import CustomUser, MealLog, ActivityLog


class FoodItemSerializer(serializers.ModelSerializer):
    """Serializer for FoodItem
    """
    class Meta:
        model = FoodItem
        fields = "__all__"


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for Activity
    """
    class Meta:
        model = Activity
        fields = "__all__"


class MealLogSerializer(serializers.ModelSerializer):
    """Serializer for MealLog
    """
    class Meta:
        model = MealLog
        fields = "__all__"


class ActivityLogSerializer(serializers.ModelSerializer):
    """Serializer for ActivityLog
    """
    class Meta:
        model = ActivityLog
        fields = "__all__"