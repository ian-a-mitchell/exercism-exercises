""" Methods for solving the Meetup exercise on Exercism. """
import datetime as dt 

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """
    Exception raised when the Meetup weekday and count do not result in a valid
    date.

    message: explanation of the error.
    """
    
    def __init__(self, message: str):
        self.message = message
    
TO_ISOWEEKDAY = {
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6,
    "sunday": 7
}

TO_WEEKEND = {
    "first": 7,
    "second": 14,
    "teenth": 19,
    "third": 21,
    "fourth": 28
}

def meetup(year: int, month: int, week: str, day_of_week: str) -> dt.date:
    """
    Method for converting a year, month, week, and day of week into a unique
    date, or raising an error if the parameters do not correspond to any day.
    
    It proceeds by calculating the weekday number of the requested day of the 
    week, using the ISO system, and finding the first and last days of the 
    weel for the given week. Then it directly calculates the difference (in
    days) between the last day of the week and the requested day, and creates
    a date corresponding to the requested date. Finally, it checks if this
    date is in fact in the requested week, and if not it will raise an
    exception as required by spec.
    
    Using the last day instead of the first as the key day makes it easier to
    handle the "last" week of the month.

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
        English day names are assumed, i.e. "Sunday", "Monday", etc.

    Returns
    -------
    dt.date
        Datetime date object containing the year, month, and day of the
        requested date.

    Raises
    ------
    MeetupDayException
        Exception raised when the Meetup weekday and count do not result in a 
        valid date.
    """
    
    last_week_day = 0
    weekday_num = TO_ISOWEEKDAY[day_of_week.casefold()]
        
    try:
        last_week_day = TO_WEEKEND[week]
    except KeyError: 
        # This triggers if the week is "last" or "fifth" and calculates the 
        # final day of the month.
        rollback = dt.timedelta(days = 1)
        new_month = month + 1
        new_year = year
        if new_month == 13:
            new_year = year + 1
            new_month = 1
        
        last_week_day = (dt.date(new_year, new_month, 1) - rollback).day
        
    # Calculates the day before the first day of the requested week.
    first_week_day = last_week_day - 7
    if week == "fifth":
        first_week_day = TO_WEEKEND["fourth"]
    
    last_day_daynum = dt.date(year, month, last_week_day).isoweekday()
    day_diff = last_day_daynum - weekday_num
    if day_diff < 0:
        day_diff = 7 + day_diff
    output = dt.date(year, month, last_week_day) - dt.timedelta(day_diff)
            
    if output.day <= first_week_day:
        raise MeetupDayException("That day does not exist.")
        
    return output