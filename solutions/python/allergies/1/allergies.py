""" Module solving the Exercism Allergies exercise. """
class Allergies:
    """ 
    Class storing the allergens a certain person is allergic to. The only
    complication is translating from the binary code representing different
    allergens to the English name of that allergen.
    """
    
    _ALGR_MASK = {
        0b1: "eggs",
        0b10: "peanuts",
        0b100: "shellfish",
        0b1000: "strawberries",
        0b10000: "tomatoes",
        0b100000: "chocolate",
        0b1000000: "pollen",
        0b10000000: "cats"
}

    def __init__(self, score: int):
        """
        Sets up Allergies object, that is, the list of allergens this person is
        allergic to.
        """
        
        self.allergens = [allergen for key, allergen 
                          in Allergies._ALGR_MASK.items()
                          if key & score == key]

    def allergic_to(self, item):
        """ 
        Returns true if item is in the list of allergens the person is allergic
        to, false otherwise.
        """
        
        return any((item == allergen for allergen in self.allergens))

    @property
    def lst(self):
        """ Returns the list of allergens this person is allergic to."""
        
        return self.allergens
