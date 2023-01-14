from django.conf.urls import url
from rest_framework import routers
from .views import (FoodItemViewSet, 
                    ActivityViewSet,
                    MealLogViewSet,
                    ActivityLogViewSet
                    # CheckBookAvailabilityAPI
                    )


urlpatterns = []

router = routers.SimpleRouter()
router.register(r'food-items',
                FoodItemViewSet, 'food_items')
router.register(r'activities',
                ActivityViewSet, 'activities')
router.register(r'users/(?P<user_id>.+)/meal-logs',
                ActivityLogViewSet, 'meal_logs')
router.register(r'users/(?P<user_id>.+)/activity-logs',
                MealLogViewSet, 'activity_logs')
# urlpatterns += url("^books/next-available/$",
#                    view=CheckBookAvailabilityAPI.as_view(),
#                     name="next-available"),
# router.register(r'users/transactions',
#                 TransactionsViewSet, 'user_transactions')
urlpatterns += router.urls

