""" Module solving the Clock exercise on Exercism. """

class Clock:
    """ 
    Class storing the time of day, without awareness of the actual day.
    Precision is limited to hours and minutes.
    """
    
    _DAY_LEN = 24
    _HR_LEN = 60
    _MIN_DAY_LEN = _DAY_LEN * _HR_LEN
    
    @staticmethod
    def _wrap_time(minutes: int) -> int:
        """
        Given a certain number of minutes (positive or negative), calculate the
        new time this represents. Time is represented as the number of minutes
        past midnight on one day, from 0 (midnight) to 1439 (one minute until
        midnight). Modular arithmetic is employed to wrap any arbitrary number
        of minutes into this timeframe.

        Parameters
        ----------
        minutes : int
            An integer representing some number of minutes (positive or not).

        Returns
        -------
        int
            The number of minutes past midnight represented by the parameter
            minutes.
        """
        new_time = minutes % Clock._MIN_DAY_LEN
        
        if new_time < 0:
            new_time += Clock._MIN_DAY_LEN
        
        return new_time
    
    @staticmethod
    def _hr_min(time: int) -> tuple[int, int]:
        """ 
        Converts a time in minutes to a time in hours and minutes. Assumes the
        time has already been wrapped into a 24-hour chunk.
        """
        
        hour, minute = divmod(time, Clock._HR_LEN)
        
        return (hour, minute)
    
    def __init__(self, hour: int, minute: int) -> None:
        """
        Sets up the time stored in this object.

        Parameters
        ----------
        hour : int
            The hour of the day. It is in 24 hour format inasmuch as values
            between 0 and 23 should be directly interpreted as times, but in
            practice can take any value and perform modular arithmetic to
            find a time fitting into a 24 hour block.
            
        minute : int
            Some number of minutes. As above this is not limited to 0-59 but
            can wrap around positively or negatively.
            
        Returns
        -------
        None
        """
                                
        self.time = Clock._wrap_time(minute + Clock._HR_LEN * hour)
        
    def __repr__(self) -> str:
        """ Representation of the Clock object if directly shown. """
        
        hour, minute = Clock._hr_min(self.time)
        
        return f'Clock({hour}, {minute})'

    def __str__(self) -> str:
        """
        String conversion of the Clock object. Follows normal digital clock
        conventions.
        """
        
        hour, minute = Clock._hr_min(self.time)
        
        return f'{hour:02}:{minute:02}'

    def __eq__(self, other) -> bool:
        """ Two clocks representing the same time are equal. """
        
        return other.time == self.time
    
    def __hash__(self):
        """ Provides the hash of this object. """
        
        return hash(self.time)

    def __add__(self, minutes: int):
        """
        Adds some number of minutes--which may be any integer value, including
        positive and negative numbers--to a Clock object.

        Parameters
        ----------
        minutes : int
            The number of minutes to shift the clock by.

        Returns
        -------
        Clock
            A new Clock object shifted by minutes minutes relative to this
            Clock.
        """
                
        return Clock(0, self.time + minutes)

    def __sub__(self, minutes: int):
        """
        Returns the time after subtracting some number of minutes. Of course,
        this is the same as adding negative minutes.
        """
        
        return self + (-minutes)
