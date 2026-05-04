class Clock:
    
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
                                
        self.hour, self.minute = Clock._new_time(minute + Clock._HR_LEN * hour)

    def __repr__(self):
        
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self):
        
        return f'{self.hour:02}:{self.minute:02}'

    def __eq__(self, other):
        
        return other.hour == self.hour and other.minute == self.minute

    def __add__(self, minutes: int):
        
        true_minutes = minutes + self.minute + self.hour * Clock._HR_LEN
                
        self.hour, self.minute = Clock._new_time(true_minutes)
        
        return self

    def __sub__(self, minutes):
        """
        Returns the time after subtracting some number of minutes. Of course,
        this is the same as adding a negative number of minutes.
        """
        
        return self + (-minutes)
