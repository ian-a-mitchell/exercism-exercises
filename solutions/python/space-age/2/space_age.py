class SpaceAge:
    """ Class for completing the Space Age exercise on Exercism.
    
    Class takes and stores an integer corresponding to the number of seconds
    since some epoch, and offers methods to represent that timeframe as
    orbital periods for every planet in the Solar System, e.g. 31 557 600 s
    corresponds to 1 Earth year. Representations are accurate to two decimals.
    """
    
    MERCURY = 'mercury'
    VENUS = 'venus'
    EARTH = 'earth'
    MARS = 'mars'
    JUPITER = 'jupiter'
    SATURN = 'saturn'
    URANUS = 'uranus'
    NEPTUNE = 'neptune'
    
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
        # Automatically generates all required functions without tedious
        # copy-pasting.
        for planet in SpaceAge.ORBITAL_PERIODS.keys():
            setattr(self, "on_" + planet, self._convert_age(planet))
        
    def _convert_age(self, planet: str) -> float:
        """
        Calculates how many orbits around the Sun a given planet will have
        made in the number of seconds specified by the age parameter.

        Parameters
        ----------
        planet : str
            A string identifying the planet to use in the calculation.

        Returns
        -------
        float
            Float giving the number of orbits around the Sun the specified
            planet will have made in the number of seconds in the object's
            age value, to two digits of precision.
        """
        # lambda planet=planet means that a *function* is returned
        # But the value is still fixed.
        return lambda planet=planet: round(
            (self.age / SpaceAge.ORBITAL_PERIODS[planet]), SpaceAge.PREC)