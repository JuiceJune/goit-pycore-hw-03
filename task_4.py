
from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.05.15"},
    {"name": "Oleh Virot", "birthday": "1990.05.10"},
    {"name": "Nick Romze", "birthday": "1990.05.09"},
    {"name": "Ann Kioki", "birthday": "1990.05.16"}
]

SATURDAY = 5
SUNDAY = 6

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        next_birthday = datetime.strptime(user.get('birthday'), '%Y.%m.%d').date().replace(year=today.year)

        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year+1)
        
        date_diff = next_birthday - today

        if date_diff.days < 7:
            if next_birthday.weekday() == SATURDAY: 
                next_birthday += timedelta(days=2)
            elif next_birthday.weekday() == SUNDAY:
                 next_birthday += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"], 
                "congratulation_date": next_birthday.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

upcoming_birthdays = get_upcoming_birthdays(users)
for item in upcoming_birthdays:
    print(f"{item['name']}: {item['congratulation_date']}")