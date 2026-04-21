"""Class and variables for solving the Robot Simulator exercise on Exercism"""
# Globals for the directions
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


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
        self.coordinates = (x_pos, y_pos)
        
    def _advance(self) -> tuple[int]:
        """
        Calculates the coordinates of the robot if it advances one step.

        Returns
        -------
        tuple[int]
            The x and y coordinates of the robot after advancing one step.
        """
        
        step = Robot._ADVANCE_TABLE[self.direction]
        
        new_x = self.coordinates[0] + step[0]
        new_y = self.coordinates[1] + step[1]
        
        return (new_x, new_y)
        
    def _turn_right(self) -> int:
        """
        Calculates the direction the robot should be facing if it turns right
        one step. If it underflows the positive values, then it wraps around 
        from east to south.

        Returns
        -------
        int
            Integer representing the direction the robot should be facing,
            using the above direction definitions.
        """
        
        new_direction = self.direction - 1
        if new_direction == -1:
            new_direction = SOUTH
        
        return new_direction
    
    def _turn_left(self) -> int:
        """
        Calculates the direction the robot should be facing if it turns left
        one step. If it overflows the positive values, then it wraps around 
        from south to east.

        Returns
        -------
        int
            Integer representing the direction the robot should be facing,
            using the above direction definitions.
        """
        
        new_direction = self.direction + 1
        if new_direction == 4:
            new_direction = EAST
        
        return new_direction
        
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
            if command == "R":
                self.direction = self._turn_right()
            elif command == "L":
                self.direction = self._turn_left()
            elif command == "A":
                self.coordinates = self._advance()
