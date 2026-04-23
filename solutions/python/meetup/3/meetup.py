""" Methods for solving the Meetup exercise on Exercism. """
from datetime import date
from calendar import monthrange, weekday 

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """
    Exception raised when the Meetup weekday and count do not result in a valid
    date.

    message: explanation of the error.
    """
    
    def __init__(self, message: str):
        self.message = message
        
WEEKDAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                 "Saturday", "Sunday"]

START_DATE = {
    "first": 1,
    "second": 8,
    "teenth": 13,
    "third": 15,
    "fourth": 22,
    "fifth": 29,
    "last": None
}

def meetup(year: int, month: int, week: str, day_of_week: str) -> date:
    """
    Method for converting a year, month, week, and day of week into a unique
    date, or raising an error if the parameters do not correspond to any day.
    
    Directly calculates the difference (in days) between the target weekday and
    the weekday of the start of the given week, then adds that difference to
    the starting day to build the output date object.

    Parameters
    ----------
    year : int
        Year of interest. The Gregorian calendar is assumed.
    month : int
        Month of interest. 1 = January, 2 = February, etc.
    week : string
        Ordinal description of the week to search. Valid values are:
            1: First (1st-7th)
            2: Second (8th-14th)
            3: Third (15th-21st)
            4: Fourth (22nd-28th)
            5: Fifth (29th-31st as applicable)
            6: Last (the last seven days of the month)
            7: Teenth (13th-19th)
    day_of_week : string
        String describing which day of the week is of interest. Ordinary 
        English-language day names are used, i.e. "Sunday", "Monday", etc.

    Returns
    -------
    date
        Datetime date object containing the year, month, and day of the
        requested date.

    Raises
    ------
    MeetupDayException
        Exception raised when:
            1: An invalid week name is provided;
            2: An invalid weekday name is provided;
            3: The requested parameters cannot be fulfilled.
    """
    
    day_of_week = day_of_week.casefold().capitalize()
    
    if week not in START_DATE:
        raise MeetupDayException(f'Unknown week provided: {week}')
    if day_of_week not in WEEKDAY_NAMES:
        raise MeetupDayException(f'Unknown weekday provided: {day_of_week}')
        
    # Since the "last" week is a None, it falls through to the second branch
    # which then calculates the date 1 week before the end of the month.
    start_day = START_DATE[week] or monthrange(year, month)[1] - 6
    
    try:
        start_wday = weekday(year, month, start_day)
        target_wday = WEEKDAY_NAMES.index(day_of_week)
        delta = (target_wday - start_wday) % 7
        return date(year, month, start_day + delta)
    except ValueError as exc:
        raise MeetupDayException("That day does not exist.") from exc