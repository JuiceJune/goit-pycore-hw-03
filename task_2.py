import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > max or quantity < min:
        return []
    
    unique_range_numbers = random.sample(range(min, max + 1), quantity)

    return sorted(unique_range_numbers)


lottery_numbers = get_numbers_ticket(1, 49, 50)
print(f"Your lottery numbers; {lottery_numbers}")