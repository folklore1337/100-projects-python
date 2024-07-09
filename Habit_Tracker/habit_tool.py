from datetime import datetime

def break_habit(habit_name, start_date, cost_per_day, minutes_wasted):
    # Личные данные
    goal = 60  # Цель в днях для избавления от привычки
    hourly_wage = 30  # Долларов в час
    
    # Рассчитать прошедшее время в секундах
    time_elapsed = (datetime.now() - start_date).total_seconds()
    
    # Конвертировать прошедшее время в часы и дни
    hours = time_elapsed / 3600
    days = hours / 24

    # Округлить до нужной точности
    hours = round(hours)
    days = round(days)

    # Рассчитать сэкономленные деньги и время
    money_saved = cost_per_day * days
    minutes_saved = round(days * minutes_wasted)
    total_money_saved = round(money_saved + (minutes_saved / 60 * hourly_wage), 2)

    # Рассчитать оставшиеся дни до достижения цели
    days_to_go = round(goal - days)
    
    # Убедиться, что оставшиеся дни не отрицательны
    if days_to_go < 0:
        days_to_go = 0

    # Форматировать вывод времени
    if hours > 72:
        time_since = f'{days} days'
    else:
        time_since = f'{hours} hours'

    return {
        'habit': habit_name,
        'time_since': time_since,
        'days_remaining': days_to_go,
        'minutes_saved': minutes_saved,
        'money_saved': f'${total_money_saved}'
    }


