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
    
    NULL = ("", 0)
    
    D_IDX = 0
    B_IDX = -1
    
    def __init__(self, capacity: int):
        """
        Sets up circular buffer (list of tuples of size capacity).
        
        Each tuple is structured to have the data item (at index 0) and a
        "birthday" (at index 1 or -1). The tuple with the smallest non-zero 
        "birthday" is perforce the oldest, while the one with the largest
        "birthday" is the youngest.

        Parameters
        ----------
        capacity : int
            Size of buffer to create.

        Returns
        -------
        None
        """
        
        self.buffer = [CircularBuffer.NULL] * capacity
        
    def _get_youngest_idx(self) -> int:
        """
        Provides the index of the youngest item in the buffer.

        Returns
        -------
        int
            Index of the youngest item in the buffer.
        """
        
        youngest = max(self.buffer, key = lambda item: item[CircularBuffer.B_IDX])
        
        return self.buffer.index(youngest)
        
    def _get_oldest_idx(self) -> int:
        """
        Provides the index of the oldest item in the buffer.

        Returns
        -------
        int
            Index of the oldest item in the buffer.
        """
        
        youngest_idx = self._get_youngest_idx()
        youngest_birthday = self.buffer[youngest_idx][CircularBuffer.B_IDX]
        
        # Finds the item with the smallest non-zero "birthday" (i.e., the
        # oldest item in the buffer)
        oldest = min(self.buffer, key = lambda item: item[CircularBuffer.B_IDX] 
                     if item[CircularBuffer.B_IDX] > 0 
                     else youngest_birthday + 1)
        
        return self.buffer.index(oldest)
    
    def _add_data(self, data, index: int) -> None:
        """
        Inserts the provided data at the provided index.

        Parameters
        ----------
        data : TYPE
            Data to insert into the buffer.
        index : int
            Location to insert the data into.

        Returns
        -------
        None
        """
        
        youngest_idx = self._get_youngest_idx()
        youngest = self.buffer[youngest_idx][CircularBuffer.B_IDX]
        
        self.buffer[index] = (data, youngest + 1)
        
    def read(self):
        """
        Returns the data value of the oldest item in the buffer and replaces it
        with a blank space. (Effectively a pop() for the oldest entry)

        Returns
        -------
        TYPE
            Data in the oldest entry (arbitrary type).

        Raises
        ------
        BufferEmptyException
            Raised if no data is available in the buffer.
        """
        
        if all((item == CircularBuffer.NULL for item in self.buffer)):
            raise BufferEmptyException("Circular buffer is empty")
            
        oldest_idx = self._get_oldest_idx()
            
        output = self.buffer[oldest_idx][CircularBuffer.D_IDX]
        self.buffer[oldest_idx] = CircularBuffer.NULL
        
        return output

    def write(self, data) -> None:
        """
        Writes data to the next available empty space in the buffer.
        
        Functions by starting at the index of the oldest entry, then iterating
        through the buffer until finding the first empty space and inserting
        the new data in its place, then quitting.

        Parameters
        ----------
        data : TYPE
            Data to insert. Any type that can be used in a tuple is acceptable.

        Returns
        -------
        None

        Raises
        ------
        BufferFullException
            Error raised if there are no empty spaces in the buffer.
        """
        if all((item != CircularBuffer.NULL for item in self.buffer)):
            raise BufferFullException("Circular buffer is full")
            
        oldest_idx = self._get_oldest_idx()
                        
        for idx in range(oldest_idx, oldest_idx + len(self.buffer)):
            new_idx = idx
            if new_idx >= len(self.buffer):
                new_idx -= len(self.buffer)
            if self.buffer[new_idx] == CircularBuffer.NULL:
                self._add_data(data, new_idx)
                break

    def overwrite(self, data) -> None:
        """
        Forcibly inserts data even if buffer is full. If there are empty
        spaces, functions as write(data), otherwise, replaces the oldest data
        in the buffer.
        
        Parameters
        ----------
        data : TYPE
            Data to insert. Any type that can be inserted into a tuple can
            be used.

        Returns
        -------
        None
        """
        
        if any((item == CircularBuffer.NULL for item in self.buffer)):
            self.write(data)
        else:
            self._add_data(data, self._get_oldest_idx())

    def clear(self) -> None:
        """ Factory reset for buffer: clears all data. """
        
        self.buffer = [CircularBuffer.NULL] * len(self.buffer)