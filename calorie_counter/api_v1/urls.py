from django.conf.urls import url
from rest_framework import routers
from .views import (FoodItemViewSet, 
                    ActivityViewSet,
                    MealLogViewSet,
                    ActivityLogViewSet,
                    CreateUserView
                    )


urlpatterns = []

router = routers.SimpleRouter()
router.register(r'users/signup',
                CreateUserView, 'signup')
router.register(r'food-items',
                FoodItemViewSet, 'food_items')
router.register(r'activities',
                ActivityViewSet, 'activities')
router.register(r'users/meal-logs',
                MealLogViewSet, 'meal_logs')
router.register(r'users/activity-logs',
                ActivityLogViewSet, 'activity_logs')
# urlpatterns += url("^books/next-available/$",
#                    view=CheckBookAvailabilityAPI.as_view(),
#                     name="next-available"),
# router.register(r'users/transactions',
#                 TransactionsViewSet, 'user_transactions')
urlpatterns += router.urls

