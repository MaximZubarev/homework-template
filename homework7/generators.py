import random
from datetime import datetime, timedelta


def all_even_numbers():
    for i in range(0, 100, 2):
        yield i


def random_increasing_number():
    number = random.randint(0, 100)

    while True:
        yield number
        number += random.randint(0, 100)


def next_day():
    day = datetime.today().date()

    while True:
        yield day

        day += timedelta(days=1)
