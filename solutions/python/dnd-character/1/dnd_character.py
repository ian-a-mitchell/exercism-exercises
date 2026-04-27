import random as rd

class Character:
    
    _DIE_SIZE = 6
    _NUM_ATT_THROWS = 4
    _NUM_ATTS = 6
    
    _ATTR_FLOOR = 3
    _ATTR_CEILING = 18
    
    @staticmethod
    def one_attribute():
        
        throws = [rd.randint(1, Character._DIE_SIZE) 
                  for _ in range(Character._NUM_ATT_THROWS)]
        
        throws.sort(reverse = True)
        throws.pop()
                
        return sum(throws)
    
    @staticmethod
    def attribute_generator():
        
        labels = ["str", "dex", "con", "int", "wis", "chr"]
        
        attributes = {label:Character.one_attribute() for label in labels}
        
        for attribute, value in attributes.items():
            if not Character._ATTR_FLOOR < value < Character._ATTR_CEILING:
                new_value = 0
                while not Character._ATTR_FLOOR < new_value < Character._ATTR_CEILING:
                    new_value = Character.one_attribute()
                attributes[attribute] = new_value
        
        return attributes
    
    def __init__(self):
        
        self.attributes = Character.attribute_generator()
        
        self.strength = self.attributes["str"]
        self.dexterity = self.attributes["dex"]
        self.constitution = self.attributes["con"]
        self.intelligence = self.attributes["int"]
        self.wisdom = self.attributes["wis"]
        self.charisma = self.attributes["chr"]
        
        self.hitpoints = 10 + modifier(self.constitution)
        
    def ability(self):
        
        idx = rd.randint(0, Character._NUM_ATTS)
        
        return list(self.attributes.values())[idx]

def modifier(value):
    
    return (value - 10) // 2
