from datetime import datetime

def get_days_from_today(date):
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Date formate should be 'YYYY-mm-dd'")
        return None

    now_date = datetime.today().date()

    delta = now_date - target_date

    return delta.days


result = get_days_from_today("2026-05-06")
print(f"result: {result} days")