class SpaceAge:
    """ Class for completing the Space Age exercise on Exercism.
    
    Class takes and stores an integer corresponding to the number of seconds
    since some epoch, and offers methods to represent that timeframe as
    orbital periods for every planet in the Solar System, e.g. 31 557 600 s
    corresponds to 1 Earth year. Representations are accurate to two decimals.
    """
    
    MERCURY = '☿'
    VENUS = '♀︎'
    EARTH = '♁'
    MARS = '♂︎'
    JUPITER = '♃'
    SATURN = '♄'
    URANUS = '⛢'
    NEPTUNE = '♆'
    
    # All data from the problem spec.
    EARTH_YEAR = 31557600
    
    ORBITAL_PERIODS = {
        MERCURY: 0.2408467 * EARTH_YEAR,
        VENUS: 0.61519726 * EARTH_YEAR,
        EARTH: EARTH_YEAR,
        MARS: 1.8808158 * EARTH_YEAR,
        JUPITER: 11.862615 * EARTH_YEAR,
        SATURN: 29.447498 * EARTH_YEAR,
        URANUS: 84.016846 * EARTH_YEAR,
        NEPTUNE: 164.79132 * EARTH_YEAR
    }
    
    PREC = 2
    
    def __init__(self, seconds: int):
        self.age = seconds
        
    def convert_age(self, planet: str) -> float:
        """
        Calculates how many orbits around the Sun a given planet will have
        made in the number of seconds specified by the age parameter.

        Parameters
        ----------
        planet : str
            A string identifying the planet to use in the calculation. Uses
            astronomical symbols rather than the common name.

        Returns
        -------
        float
            Float giving the number of orbits around the Sun the specified
            planet will have made in the number of seconds in the object's
            age value, to two digits of precision.
        """
        
        return round((self.age / SpaceAge.ORBITAL_PERIODS[planet]),
                     SpaceAge.PREC)
        
    def on_mercury(self) -> float:
        """
        This method, like all of the other planet-specific methods, is a shell
        around the convert_age method. Refer to that method for details.
        
        Because every planet-specific method is identical other than the named
        planet, I omit docstrings for them.
        """
        
        return self.convert_age(SpaceAge.MERCURY)
    
    def on_venus(self) -> float:
        
        return self.convert_age(SpaceAge.VENUS)
    
    def on_earth(self) -> float:
        
        return self.convert_age(SpaceAge.EARTH)
    
    def on_mars(self) -> float:
        
        return self.convert_age(SpaceAge.MARS)
    
    def on_jupiter(self) -> float:
        
        return self.convert_age(SpaceAge.JUPITER)
    
    def on_saturn(self) -> float:
        
        return self.convert_age(SpaceAge.SATURN)
    
    def on_uranus(self) -> float:
        
        return self.convert_age(SpaceAge.URANUS)
    
    def on_neptune(self) -> float:
        
        return self.convert_age(SpaceAge.NEPTUNE)
