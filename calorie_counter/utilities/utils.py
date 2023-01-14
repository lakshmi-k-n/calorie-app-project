from users.models import CustomUser, MealLog, ActivityLog


def get_calorie_expenditure(user, year, month=None, week=None, day=None):
    logs = ActivityLog.objects.filter(user=user,created_at__year=year)
    if month:
        logs = logs.filter(created_at__month=month)
    if week:
        logs = logs.filter(created_at__week=week)
    if day:
        logs = logs.filter(created_at__month=day)
    calories_list = logs.values_list("calories",flat=True)
    total = sum(calories_list)
    return  total


def get_calorie_consumption(user, year, month=None, week=None, day=None):
    logs = MealLog.objects.filter(user=user,created_at__year=year)
    if month:
        logs = logs.filter(created_at__month=month)
    if week:
        logs = logs.filter(created_at__week=week)
    if day:
        logs = logs.filter(created_at__month=day)
    calories_list = logs.values_list("calories",flat=True)
    total = sum(calories_list)
    return  total