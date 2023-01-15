from users.models import CustomUser, MealLog, ActivityLog


def get_calorie_expenditure(user, year, month=None, week=None, day=None):
    logs = ActivityLog.objects.filter(user=user,created_at__year=year)
    if month:
        logs = logs.filter(created_at__month=month)
    if week:
        logs = logs.filter(created_at__week=week)
    if day:
        logs = logs.filter(created_at__day=day)
    calories_list = logs.values_list("calories_burnt",flat=True)
    total = sum(calories_list)
    return  total


def get_calorie_consumption(user, year, month=None, week=None, day=None):
    logs = MealLog.objects.filter(user=user,created_at__year=year)
    if month:
        logs = logs.filter(created_at__month=month)
    if week:
        logs = logs.filter(created_at__week=week)
    if day:
        logs = logs.filter(created_at__day=day)
    calories_list = logs.values_list("total_calories_consumed",flat=True)
    total = sum(calories_list)
    return  total


def get_total_calories_per_meal(std_calories, weight):
    total = (std_calories / 100) * weight
    return total


def get_total_expense_per_activity(std_calories, duration):
    total = (std_calories / 30) * duration
    return total