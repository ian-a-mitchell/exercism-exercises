"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0
    BASE_HEALTH = 3
    
    def __init__(self, x_input, y_input):
        self.x_coordinate = x_input
        self.y_coordinate = y_input
        self.health = Alien.BASE_HEALTH
        
        Alien.total_aliens_created += 1
        
    def hit(self):
        self.health -= 1
            
    def is_alive(self):
        return self.health > 0
    
    def teleport(self, x_input, y_input):
        self.x_coordinate = x_input
        self.y_coordinate = y_input
        
    def collision_detection(self, other):
        pass


def new_aliens_collection(positions):
    
    return list(map(lambda position: Alien(position[0], position[1]), positions))
