import time
from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    today = date.today()
    next_week = today + timedelta(days=7)
    # Перевірка на порожній список користувачів
    if not users:
        return {}

    birthdays_per_week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
    }

    # Створюємо словник для відображення днів тижня
    days_of_week = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday',
    }

    upcoming_birthdays = {}  # Пустий словник для майбутніх днів народження

    for user in users:
        name = user['name']
        birthday = user['birthday']

        # Визначаємо день народження наступного тижня
        next_birthday = birthday.replace(year=today.year)

        if next_birthday < today:
            # Якщо день народження вже минув в поточному році, перевіряємо, чи він наступає в новому році
            next_birthday = birthday.replace(year=today.year + 1)

        if today <= next_birthday <= next_week:
            # Визначаємо день тижня для дня народження
            day_of_week = next_birthday.strftime('%A')

            if day_of_week not in ['Saturday', 'Sunday']:
                # Якщо день народження не припадає на вихідний, додаємо його до словника
                if day_of_week not in upcoming_birthdays:
                    upcoming_birthdays[day_of_week] = [name]
                else:
                    upcoming_birthdays[day_of_week].append(name)
            if day_of_week in ['Saturday', 'Sunday']:
                day_of_week = 'Monday'
                # Якщо день народження не припадає на вихідний, додаємо його до словника
                if day_of_week not in upcoming_birthdays:
                    upcoming_birthdays[day_of_week] = [name]
                else:
                    upcoming_birthdays[day_of_week].append(name)

    if not upcoming_birthdays:
        return {}  # Якщо немає майбутніх днів народження, повертаємо пустий словник

    return upcoming_birthdays


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 9, 9).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
