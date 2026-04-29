"""
Module implementing a circular buffer and related exceptions for the Exercism
exercise.
"""

class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.msg = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    
    def __init__(self, message):
        self.msg = message


class CircularBuffer:
    """
    Class implementing a circular buffer for the Exercism exercise.
    """
    
    def __init__(self, capacity: int):
        """
        Sets up circular buffer.

        Parameters
        ----------
        capacity : int
            Size of buffer to create.

        Returns
        -------
        None
        """
        
        self.buffer = []
        self.capacity = capacity
        
    def read(self):
        """
        Pops the oldest (first) entry in the buffer.

        Returns
        -------
        TYPE
            Data in the oldest entry (arbitrary type).

        Raises
        ------
        BufferEmptyException
            Raised if no data is available in the buffer.
        """
        
        if not self.buffer:
            raise BufferEmptyException("Circular buffer is empty")
            
        return self.buffer.pop(0)

    def write(self, data) -> None:
        """
        Writes data to the next available empty space in the buffer.

        Parameters
        ----------
        data : TYPE
            Data to insert.

        Returns
        -------
        None

        Raises
        ------
        BufferFullException
            Error raised if there are no empty spaces in the buffer.
        """
        if len(self.buffer) == self.capacity:
            raise BufferFullException("Circular buffer is full")
            
        self.buffer.append(data)

    def overwrite(self, data) -> None:
        """
        Forcibly inserts data even if buffer is full. If there are empty
        spaces, functions as write(data), otherwise, replaces the oldest data
        in the buffer.
        
        Parameters
        ----------
        data : TYPE
            Data to insert.

        Returns
        -------
        None
        """
        
        if len(self.buffer) == self.capacity:
            self.buffer.pop(0)
            
        self.write(data)

    def clear(self) -> None:
        """ Factory reset for buffer: clears all data. """
        
        self.buffer = []