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
    
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.health = Alien.BASE_HEALTH
        
        Alien.total_aliens_created += 1
        
    def hit(self):
        if self.health > 0:
            self.health -= 1
            
    def is_alive(self):
        alive = True
        
        if self.health < 1:
            alive = False
            
        return alive
    
    def teleport(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        
    def collision_detection(self, other):
        pass


def new_aliens_collection(alien_start_positions):
    
    output = []
    
    for coordinate in alien_start_positions:
        x = coordinate[0]
        y = coordinate [1]
        output.append(Alien(x, y))
        
    return output