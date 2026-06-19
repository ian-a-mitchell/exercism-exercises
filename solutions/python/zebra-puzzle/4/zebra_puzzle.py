"""
Module solving the Zebra Puzzle. This is a puzzle of logical deduction based
on the following fifteen clues:
    1: There are five houses.
    2: The Englishman lives in the red house.
    3: The Spaniard owns the dog.
    4: The person in the green house drinks coffee.
    5: The Ukrainian drinks tea.
    6: The green house is immediately to the right of the ivory house.
    7: The snail owner likes to go dancing.
    8: The person in the yellow house is a painter.
    9: The person in the middle house drinks milk.
    10: The Norwegian lives in the first house.
    11: The person who enjoys reading lives in the house next to the person 
        with the fox.
    12: The painter's house is next to the house with the horse.
    13: The person who plays football drinks orange juice.
    14: The Japanese person plays chess.
    15: The Norwegian lives next to the blue house.

Given these, we are to discover:
    1: Who (that is, the person of which nationality) drinks water?
    2: Who has a zebra for a pet?
    
Since there are five classes of information (nationality, house color, pet,
favorite drink, and favorite hobby), which each need to be filled in for five
"positions," the total number of possiblities disregarding the clues is 5!^5,
or about 25 billion. Therefore, some logical deductions must be made to enable
reasonable performance.
"""
    
from itertools import permutations
from functools import cache
from random import sample

_NATIONS = ("Norwegian", "Englishman", "Ukranian", "Japanese", "Spaniard")
_COLORS = ("Yellow", "Red", "Blue", "Green", "Ivory")
_PETS = ("Zebra", "Fox", "Dog", "Horse", "Snail")
_HOBBIES = ("Chess", "Football", "Reading", "Dancing", "Painter")
_DRINKS = ("Orange juice", "Milk", "Tea", "Coffee", "Water")

_NUM_HOUSES = 5
        
@cache
def solve():
    """
    Function solving the Zebra Puzzle, essentially. Works through a combination
    of search and logical deduction--the six simplest clues:
        1: There are five houses.
        8: The person in the yellow house is a painter.
        9: The person in the middle house drinks milk.
        10: The Norwegian lives in the first house.
        12: The painter's house is next to the house with the horse.
        15: The Norwegian lives next to the blue house.
    along with the auxiliary clues:
        2: The Englishman lives in the red house.
        6: The green house is immediately to the right of the ivory house.
    are used to set certain fixed values, substantailly reducing the search
    space and eliminating the ned to check whether those clues are fulfilled.
    However, the other clues and values are left to be permuted over rather
    than the logical deduction being carried to its full extent. This provides
    an enormous speedup over a naive search, and even a roughly 20x speedup
    over a search with eager validation.
    
    Note that the search and validation works with indices and not the values
    directly, which provided a significant speedup in testing, and that the
    ordering of the underlying data is randomized at the start to show that the
    success of the algorithm does not depend on a special data ordering.
    
    Parameters:
        None
    
    Returns:
        list[dict[str: str]]
            A list of dictionaries, each dictionary containing all of the
            information on the inhabitats of each house. The index corresponds
            to the house number and is assumed to increase left to right.
    """
    
    nationalities = sample(_NATIONS, k = len(_NATIONS))
    house_colors = sample(_COLORS, k = len(_COLORS))
    house_pets = sample(_PETS, k = len(_PETS))
    fav_drinks = sample(_DRINKS, k =len(_DRINKS))
    fav_hob = sample(_HOBBIES, k = len(_HOBBIES))
    
    norwegian = nationalities.index("Norwegian")
    englishman = nationalities.index("Englishman")
    ukranian = nationalities.index("Ukranian")
    japanese = nationalities.index("Japanese")
    spaniard = nationalities.index("Spaniard")
    yellow = house_colors.index("Yellow")
    red = house_colors.index("Red")
    blue = house_colors.index("Blue")
    green = house_colors.index("Green")
    ivory = house_colors.index("Ivory")
    fox = house_pets.index("Fox")
    horse = house_pets.index("Horse")
    snail = house_pets.index("Snail")
    dog = house_pets.index("Dog")
    zebra = house_pets.index("Zebra")
    orange_juice = fav_drinks.index("Orange juice")
    milk = fav_drinks.index("Milk")
    tea = fav_drinks.index("Tea")
    coffee = fav_drinks.index("Coffee")
    water = fav_drinks.index("Water")
    chess = fav_hob.index("Chess")
    football = fav_hob.index("Football")
    reading = fav_hob.index("Reading")
    dancing = fav_hob.index("Dancing")
    painter = fav_hob.index("Painter")
    
    nat_idx = [englishman, ukranian, japanese, spaniard]
    color_idx = [red, green, ivory]
    pet_idx = [fox, snail, dog, zebra]
    drink_idx = [orange_juice, tea, coffee, water]
    hobby_idx = [chess, football, reading, dancing]

    def known3(nations, pets):
        """ Helper function to validate that clue 3 is followed. """
        return any(nations[idx] == spaniard and pets[idx] == dog 
                   for idx in range(len(nations)))
    
    def validate_colors(nations, colors):
        """ Helper function to validate that clues 2 and 6 are followed. """
        known2 = any(nations[idx] == englishman 
                     and colors[idx] == red 
                     for idx in range(len(nations)))
        known6 = any(colors[idx] == ivory 
                     and colors[idx + 1] == green
                     for idx in range(len(colors) - 1))
        
        return known2 and known6
    
    def validate_drinks(nations, colors, drinks):
        """ Helper function to validate that clues 4 and 5 are followed. """
        known4 = any(colors[idx] == green 
                     and drinks[idx] == coffee 
                     for idx in range(len(colors)))
        known5 = any(nations[idx] == ukranian 
                     and drinks[idx] == tea 
                     for idx in range(len(nations)))
        return known4 and known5
    
    def validate_hobbies(nations, drinks, pets, hobbies):
        """ 
        Helper function to validate that clues 7, 11, 13, and 14 are followed.
        """
        known7 = any(pets[idx] == snail 
                     and hobbies[idx] == dancing
                     for idx in range(len(pets)))
        known11 = any(pets[idx] == fox and hobbies[idx + 1] == reading
                      for idx in range(len(pets) - 1)) or any(
                      pets[idx] == fox and hobbies[idx - 1] == reading
                      for idx in range(1, len(pets)))
        known13 = any(hobbies[idx] == football
                      and drinks[idx] == orange_juice 
                      for idx in range(len(drinks)))
        known14 = any(nations[idx] == japanese 
                      and hobbies[idx] == chess
                      for idx in range(len(nations)))
        
        return known7 and known11 and known13 and known14
    
    for nat_per in permutations(nat_idx):
        nation = [norwegian] + list(nat_per)
        for col_per in permutations(color_idx):
            color = [yellow, blue] + list(col_per)
            if validate_colors(nation, color):
                for pet_per in permutations(pet_idx):
                    pet = [pet_per[0]] + [horse] + list(pet_per[1:])
                    if known3(nation, pet):
                        for dr_per in permutations(drink_idx):
                            drink = list(dr_per[0:2]) + [milk] + list(dr_per[2:])
                            if validate_drinks(nation, color, drink):
                                for hob_per in permutations(hobby_idx):
                                    hobby = [painter] + list(hob_per)
                                    if validate_hobbies(nation, drink, pet, hobby):
                                        houses = [
                                            {
                                                "Nation": nationalities[nation[idx]],
                                                "Color": house_colors[color[idx]],
                                                "Pet": house_pets[pet[idx]],
                                                "Drink": fav_drinks[drink[idx]],
                                                "Hobby": fav_hob[hobby[idx]]
                                            } for idx in range(_NUM_HOUSES)]
                                        return houses
    return None

def drinks_water():
    """ Returns the water drinker's nationality. """
    solution = solve()
    for house in solution:
        if house["Drink"] == "Water":
            return house["Nation"]
    return None

def owns_zebra():
    """ Returns the zebra owner's nationality. """
    solution = solve()
    for house in solution:
        if house["Pet"] == "Zebra":
            return house["Nation"]
    return None