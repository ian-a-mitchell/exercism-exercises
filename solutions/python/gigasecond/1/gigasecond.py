""" Method for solving Gigasecond problem on Exercism. """
import datetime as dt

def add(moment: dt.datetime, difference: int = 1e9) -> dt.datetime:
    """
    Calculates the precise time and date a given number of seconds (by default
    positive one billion) from the given date and time; supports both addition
    and subtraction.

    Parameters
    ----------
    moment : dt.datetime
        The given date and time.
    difference : int, optional
        The offset in signed seconds. The default is 1e9 seconds.

    Returns
    -------
    dt.datetime
        The date and time difference seconds after (or before) moment.
    """
        
    return moment + dt.timedelta(seconds = difference)
