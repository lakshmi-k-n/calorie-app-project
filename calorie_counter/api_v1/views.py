# from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from food.models import FoodItem, Activity
from users.models import CustomUser, MealLog, ActivityLog
from .serializers import (FoodItemSerializer, ActivitySerializer,
                            MealLogSerializer, ActivityLogSerializer)
from utilities.utils import get_calorie_consumption, get_calorie_expenditure
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.http.response import Http404
# Create your views here.


class FoodItemViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    '''
    View to list books
    '''
    permission_classes = (IsAuthenticated,)
    renderer_classes = (CamelCaseJSONRenderer,)
    authentication_classes = (BasicAuthentication,)
    serializer_class = FoodItemSerializer
    lookup_field = ('id')

    def get_queryset(self):
        food_items = FoodItem.objects.all().order_by("-id")
        return food_items


class ActivityViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    '''
    View to list books
    '''
    permission_classes = (IsAuthenticated,)
    renderer_classes = (CamelCaseJSONRenderer,)
    authentication_classes = (BasicAuthentication,)
    serializer_class = ActivitySerializer
    lookup_field = ('id')

    def get_queryset(self):
        activities = Activity.objects.all().order_by("-id")
        return activities


class ActivityLogViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    '''
    View to list books
    '''
    permission_classes = (IsAuthenticated,)
    renderer_classes = (CamelCaseJSONRenderer,)
    authentication_classes = (BasicAuthentication,)
    serializer_class = ActivityLogSerializer
    lookup_field = ('id')

    def get_queryset(self):
        activities = ActivityLog.objects.all().order_by("-id")
        return activities

    @action(detail=True, methods=['get'])
    def stats(self, request, **kwargs):
        user_id = kwargs.get('user_id',None)
        if not user_id:
            raise Http404
        frame = self.request.query_params.get('frame', None)
        day = self.request.query_params.get('day', None)
        week = self.request.query_params.get('week', None)
        month = self.request.query_params.get('month', None)
        year = self.request.query_params.get('year', None)
        calorie_expenditure = 0
        if frame == "daily" and day and month and year:
            calorie_expenditure = \
                    get_calorie_expenditure(year, month=month,
                                             day=day)
        elif frame == "weekly" and week and year:
            # need week and year
            calorie_expenditure = get_calorie_expenditure(year, week=week)
        elif frame == "monthly" and month and year:
            # need month and year
            calorie_expenditure = get_calorie_expenditure(year, month=month)
        else:
            raise Http404
        active_transactions = Transaction.objects.filter(user=user_id,
                                                    is_active=True
                                                    ).order_by('-id')

        serializer = self.serializer_class(active_transactions, many=True)
        return Response(serializer.data)


class MealLogViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    '''
    View to list books
    '''
    permission_classes = (IsAuthenticated,)
    renderer_classes = (CamelCaseJSONRenderer,)
    authentication_classes = (BasicAuthentication,)
    serializer_class = MealLogSerializer
    lookup_field = ('id')

    def get_queryset(self):
        meal_logs = MealLog.objects.all().order_by("-id")
        return meal_logs

    @action(detail=True, methods=['get'])
    def stats(self, request, **kwargs):
        user_id = kwargs.get('user_id',None)
        if not user_id:
            raise Http404
        frame = self.request.query_params.get('frame', None)
        day = self.request.query_params.get('frame', None)
        week = self.request.query_params.get('frame', None)
        month = self.request.query_params.get('frame', None)
        year = self.request.query_params.get('frame', None)

        if frame == "daily":
            # need day,month,year
            get_calorie_consumption(year, month=month, day=day)
        elif frame == "weekly":
            # need week and year
            get_calorie_consumption(year, week=week)
        elif frame == "monthly":
            # need month and year
            get_calorie_consumption(year, month=month)
            pass
        else:
            raise Http404
        active_transactions = Transaction.objects.filter(user=user_id,
                                                    is_active=True
                                                    ).order_by('-id')

        serializer = self.serializer_class(active_transactions, many=True)
        return Response(serializer.data)
