import datetime
from datetime import date
import msg
import math


def get_period(start, frequency):
    if type(start) != datetime.date:
        return msg("Error: Argument 'start' must be a Date object")

    starting_year = int(start[0:4])

    if frequency == 1:
        return starting_year

    starting_month = int(start[5:8])

    if frequency == 12:
        return [starting_year, starting_month]

    if frequency == 4:
        starting_quarter = math.ceil(starting_month/3)
        return [starting_year, starting_quarter]

    if frequency == 52 or frequency == 365:
        return 1