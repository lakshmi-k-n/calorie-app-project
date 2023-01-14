# from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from food.models import FoodItem, Activity
from users.models import CustomUser, MealLog, ActivityLog
from .serializers import (FoodItemAdminSerializer, FoodItemMemberSerializer,
                            ActivityAdminSerializer, ActivityMemberSerializer,
                            MealLogSerializer, ActivityLogSerializer,
                            UserSerializer)
from utilities.utils import (get_calorie_consumption, get_calorie_expenditure,
                                get_total_calories_per_meal,
                                get_total_expense_per_activity)
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.http.response import Http404
from django.db.models import Q

# Create your views here.



class CreateUserView(mixins.CreateModelMixin, 
                        viewsets.GenericViewSet):
    serializer_class = UserSerializer


class ActivityViewSet(mixins.CreateModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    '''
    '''
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication,)
    # serializer_class = FoodItemSerializer
    lookup_field = ('id')

    def get_serializer_class(self):
        """
        Different serializations depending on the incoming request.
        Admins get full serialization, members get restricted serialization
        """
        user = self.request.user
        if user.groups.filter(name='admin').exists():
            return ActivityAdminSerializer
        else:
            return ActivityMemberSerializer

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='admin').exists():
            return Activity.objects.all().order_by("-id")
        else:
            activities = Activity.objects.filter(
            Q(is_global=True) | Q(created_by=user))
            return set(activities)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)


class FoodItemViewSet(mixins.CreateModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    '''
    '''
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication,)
    # serializer_class = FoodItemSerializer
    lookup_field = ('id')

    def get_serializer_class(self):
        """
        Different serializations depending on the incoming request.
        Admins get full serialization, members get restricted serialization
        """
        user = self.request.user
        if user.groups.filter(name='admin').exists():
            return FoodItemAdminSerializer
        else:
            return FoodItemMemberSerializer

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='admin').exists():
            return FoodItem.objects.all().order_by("-id")
        else:
            food_items = FoodItem.objects.filter(
            Q(is_global=True) | Q(created_by=user))
            return set(food_items)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)


class ActivityLogViewSet(mixins.CreateModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    '''
    View to list books
    '''
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication,)
    serializer_class = ActivityLogSerializer
    lookup_field = ('id')

    def get_queryset(self):
        user = self.request.user
        activities = ActivityLog.objects.filter(user=user
                                        ).order_by("-id")
        return activities

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)

    @action(detail=True, methods=['get'])
    def stats(self, request, **kwargs):
        user = self.request.user
        frame = self.request.query_params.get('frame', None)
        day = self.request.query_params.get('day', None)
        week = self.request.query_params.get('week', None)
        month = self.request.query_params.get('month', None)
        year = self.request.query_params.get('year', None)
        calorie_expenditure = 0
        if frame == "daily" and day and month and year:
            calorie_expenditure = \
                    get_calorie_expenditure(user, year, month=month,
                                             day=day)
        elif frame == "weekly" and week and year:
            # need week and year
            calorie_expenditure = get_calorie_expenditure(user, year, week=week)
        elif frame == "monthly" and month and year:
            # need month and year
            calorie_expenditure = get_calorie_expenditure(user, year, month=month)
        else:
            raise Http404
        return Response(serializer.data)


class MealLogViewSet(mixins.CreateModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    '''
    View to list meal logs
    '''
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication,)
    serializer_class = MealLogSerializer
    lookup_field = ('id')

    def get_queryset(self):
        user = self.request.user
        meal_logs = MealLog.objects.filter(user=user).order_by("-id")
        return meal_logs

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)

    @action(detail=True, methods=['get'])
    def stats(self, request, **kwargs):
        user = self.request.user
        frame = self.request.query_params.get('frame', None)
        day = self.request.query_params.get('day', None)
        week = self.request.query_params.get('week', None)
        month = self.request.query_params.get('month', None)
        year = self.request.query_params.get('year', None)

        if frame == "daily":
            # need day,month,year
            get_calorie_consumption(user, year, month=month, day=day)
        elif frame == "weekly":
            # need week and year
            get_calorie_consumption(user, year, week=week)
        elif frame == "monthly":
            # need month and year
            get_calorie_consumption(user, year, month=month)
            pass
        else:
            raise Http404
        return Response(serializer.data)
