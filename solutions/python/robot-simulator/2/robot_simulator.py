"""Class and variables for solving the Robot Simulator exercise on Exercism"""
# Globals for the directions
EAST = 90
NORTH = 0
WEST = 270
SOUTH = 180


class Robot:
    """
    The class to be implemented as part of the Robot Simulator Exercism
    exercise. It has methods to simulate a robot moving around a grid.
    """
    
    # The change in x and y coordinates from the robot taking one step, by the
    # current direction
    _ADVANCE_TABLE = {
        EAST: (1, 0),
        NORTH: (0, 1),
        WEST: (-1, 0),
        SOUTH: (0, -1)
    }
    
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        """
        Initializes the robot to be located at a certain point and facing a
        certain direction.

        Parameters
        ----------
        direction : int, optional
            Integer corresponding to the direction the robot is facing. The 
            default is NORTH.
        x_pos : int, optional
            The starting x-coordinate of the robot, increasing to the east and
            decreasing to the west. The default is 0.
        y_pos : int, optional
            The starting y-coordinate of the robot, increasing to the north and
            decreasing to the south. The default is 0.

        Returns
        -------
        None
        """
        
        self.direction = direction
        self.x_coor = x_pos
        self.y_coor = y_pos
        
        self._commands = {
            "R": self._turn_right,
            "L": self._turn_left,
            "A": self._advance
        }
        
    @property
    def coordinates(self) -> tuple[int]:
        """ Returns tuple of (x_coor, y_coor) as required by program spec."""
        
        return (self.x_coor, self.y_coor)
        
    def _advance(self) -> None:
        """
        Calculates the coordinates of the robot if it advances one step.

        Returns
        -------
        tuple[int]
            The x and y coordinates of the robot after advancing one step.
        """
        
        step = Robot._ADVANCE_TABLE[self.direction]
        
        self.x_coor = self.x_coor + step[0]
        self.y_coor = self.y_coor + step[1]
        
    def _turn_right(self) -> None:
        """
        Calculates the direction the robot should be facing if it turns right
        one step.

        Returns
        -------
        int
            Integer representing the direction the robot should be facing,
            using the above direction definitions.
        """
        
        self.direction = (self.direction + 90) % 360
            
    def _turn_left(self) -> None:
        """
        Calculates the direction the robot should be facing if it turns left
        one step.

        Returns
        -------
        int
            Integer representing the direction the robot should be facing,
            using the above direction definitions.
        """
        
        self.direction = (self.direction - 90) % 360
        
    def move(self, commands: str) -> None:
        """
        Given a string of commands, causes the simulated robot to execute those
        commands (update its direction and coordinates parameters)

        Parameters
        ----------
        commands : str
            A string of commands. Valid commands are:
                "R": Robot turns right;
                "L": Robot turns left;
                "A": Robot advances one step

        Returns
        -------
        None; method updates robot's internal state
        """
        
        for command in commands:
            self._commands[command]()
