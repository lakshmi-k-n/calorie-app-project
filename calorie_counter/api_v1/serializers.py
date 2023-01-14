from rest_framework import serializers
from food.models import FoodItem, Activity
from users.models import CustomUser, MealLog, ActivityLog
from django.contrib.auth.models import Group


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User
    """
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ("id","email","username","password",
                    "age","height","weight")
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def create(self, validated_data):

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            age=validated_data['age'],
            height=validated_data['height'],
            weight=validated_data['weight'],

        )
        try:
            group = Group.objects.filter(name='member').get()
        except Group.ObjectDoesNotExist:
            raise Http404
        user.groups.add(group)
        return user


class FoodItemAdminSerializer(serializers.ModelSerializer):
    """Serializer for FoodItem
    """
    class Meta:
        model = FoodItem
        fields = "__all__"
        extra_kwargs = {
            'created_by': {'read_only': True},
        }

class FoodItemMemberSerializer(serializers.ModelSerializer):
    """Serializer for FoodItem
    """
    class Meta:
        model = FoodItem
        fields = "__all__"
        extra_kwargs = {
            'created_by': {'read_only': True},
            'is_global': {'read_only': True},
            'is_active': {'read_only': True},

        }


class ActivityAdminSerializer(serializers.ModelSerializer):
    """Serializer for Activity
    """
    class Meta:
        model = Activity
        fields = "__all__"
        extra_kwargs = {
            'created_by': {'read_only': True},
        }


class ActivityMemberSerializer(serializers.ModelSerializer):
    """Serializer for Activity
    """
    class Meta:
        model = Activity
        fields = "__all__"
        extra_kwargs = {
            'created_by': {'read_only': True},
            'is_global': {'read_only': True},
            'is_active': {'read_only': True},

        }


class MealLogSerializer(serializers.ModelSerializer):
    """Serializer for MealLog
    """
    class Meta:
        model = MealLog
        fields = "__all__"
        extra_kwargs = {
            'user': {'read_only': True},
            'total_calories_consumed': {'read_only': True},
        }


class ActivityLogSerializer(serializers.ModelSerializer):
    """Serializer for ActivityLog
    """
    class Meta:
        model = ActivityLog
        fields = "__all__"
        extra_kwargs = {
            'user': {'read_only': True},
            'calories_burnt': {'read_only': True},
        }