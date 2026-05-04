""" Module solving the Clock exercise on Exercism. """

class Clock:
    """ 
    Class storing the time of day, without awareness of the actual day.
    Precision is limited to hours and minutes.
    """
    
    _DAY_LEN = 24
    _HR_LEN = 60
    
    @staticmethod
    def _new_time(minutes: int) -> tuple[int, int]:
        """
        Given a certain number of minutes (positive or negative), calculate the
        new time this represents.

        Parameters
        ----------
        minutes : int
            An integer representing some number of minutes (positive or not).

        Returns
        -------
        tuple[int, int]
            A tuple representing the hours and minutes parts of a time.
        """
        new_hour, new_minute = divmod(minutes, Clock._HR_LEN)
        
        if new_minute < 0:
            new_hour -= 1
            new_minute += Clock._HR_LEN
            
        new_hour %= Clock._DAY_LEN
        
        if new_hour < 0:
            new_hour += Clock._DAY_LEN
        
        return (new_hour, new_minute)
    
    def __init__(self, hour: int, minute: int) -> None:
        """
        Sets up the time stored in this object.

        Parameters
        ----------
        hour : int
            The hour of the day. It is in 24 hour format inasmuch as values
            between 0 and 23 should be directly interpreted as times, but in
            practice can take any value and perform modular arithmetic to
            convert it into a valid hours value.
            
        minute : int
            Some number of minutes. As above this is not limited to 0-59 but
            can wrap around positively or negatively.
            
        Returns
        -------
        None
        """
                                
        self.hour, self.minute = Clock._new_time(minute + Clock._HR_LEN * hour)

    def __repr__(self):
        """ Representation of the Clock object if directly shown. """
        
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self):
        """
        String conversion of the Clock object. Follows normal digital clock
        conventions.
        """
        
        return f'{self.hour:02}:{self.minute:02}'

    def __eq__(self, other):
        """ Two clocks representing the same time are equal. """
        
        return other.hour == self.hour and other.minute == self.minute
    
    def __hash__(self):
        
        return hash(self.hour + self.minute)

    def __add__(self, minutes: int):
        """
        Adds some number of minutes--which may be any integer value, including
        positive and negative numbers--to a Clock object. Since the number of
        minutes is arbitrary, this function must support full wrap-around to
        an arbitrary degree.

        Parameters
        ----------
        minutes : int
            The number of minutes to shift the clock by.

        Returns
        -------
        Clock
            A new Clock object shifted by minutes minutes relative to this
            Clock. Includes full wrap-around support.
        """
        
        true_minutes = minutes + self.minute + self.hour * Clock._HR_LEN
                
        new_hour, new_minute = Clock._new_time(true_minutes)
        
        return Clock(new_hour, new_minute)

    def __sub__(self, minutes):
        """
        Returns the time after subtracting some number of minutes. Of course,
        this is the same as adding a negative number of minutes.
        """
        
        return self + (-minutes)
