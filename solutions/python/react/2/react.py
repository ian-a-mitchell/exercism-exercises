""" Module solving the React exercise on Exercism. Largely copied work. """

class Cell:
    """
    Superclass for the InputCell and ComputeCell classes. Critically, defines
    data structures and methods for keeping track of dependent cells and
    pushing updates when necessary.
    """
    def __init__(self, initial_value: any):
        """
        Sets up the Cell by initializing its internal value and a set of
        dependent cells (at this point an empty set).

        Parameters
        ----------
        initial_value : any
            Data to store in the cell.

        Returns
        -------
        None
        """
        
        self._value = initial_value
        self._listeners = set()
        
    def add_listener(self, cell):
        """
        Adds a dependent cell that needs to be notified of updates to this cell
        to the _listeners set.

        Parameters
        ----------
        cell : Cell
            Cell to be added to the _listeners set.

        Returns
        -------
        None
        """
        
        self._listeners.add(cell)
        
    def notify_listeners(self, changed: dict):
        """
        Functions as a kind of summons to all of the Cells in _listeners to do
        something (recompute their value) given a dictionary of Cells and their
        previous values (that is, the variable changed)

        Parameters
        ----------
        changed : dict[Cell, data]
            A dictionary of Cell objects and associated values. Generally these
            values are the previous values of the Cell

        Returns
        -------
        None
        """
        
        for listener in self._listeners:
            listener.recompute(changed)
            
    @property
    def value(self):
        """ Simply a wrapper for self._value to work with the tests. """
        
        return self._value
            
class InputCell(Cell):
    """
    Subclass of Cell that implements a method relevant to InputCells, that is,
    Cells that store data. Per the tests, this is to trigger updates for all
    dependent cells if the InputCell has a data update.
    """
    
    @Cell.value.setter
    def value(self, value: any):
        """
        Wrapper pseudo-property that implements a setter function for the
        _value of InputCells. This calls notify_listeners and uses a tricky
        bit of shared memory (the changed dictionary) to both update all
        dependent cells and trigger any necessary callbacks.

        Parameters
        ----------
        value : any
            The new value of the cell.

        Returns
        -------
        None
        """
        
        if value != self._value:
            self._value = value
            changed = {}
            self.notify_listeners(changed)
            for cell, original_value in changed.items():
                if cell.value != original_value:
                    cell.call_callbacks()

class ComputeCell(Cell):
    """
    Subclass of Cell implementing ComputeCell functionality. ComputeCells are
    meant to apply an arbitrary function to a set of InputCells, and be updated
    if the value of the InputCell changes. If their value changes, they are
    also supposed to trigger callbacks...whatever those are meant to be
    conceptually.
    """
    
    def __init__(self, inputs: list[InputCell], compute_function):
        """
        Sets up a ComputeCell given inputs and a function to use.

        Parameters
        ----------
        inputs : list[InputCell]
            A list of InputCells to use as inputs to compute_function.
        compute_function : function
            A function to use on the inputs. Note that there is no error
            handling to ensure that the inputs and function fit together.

        Returns
        -------
        None
        """
        
        self._inputs = inputs
        self._compute_function = compute_function
        self._callbacks = set()
        
        # Connects this cell to all of its input cells to get updates
        for inp in self._inputs:
            inp.add_listener(self)
        
        # Actually sets up the value of this cell
        super().__init__(self.compute())
        
    def compute(self):
        """ A simple wrapper for compute_function being applied to inputs. """
        return self._compute_function([inp.value for inp in self._inputs])
    
    def recompute(self, changed: dict):
        """
        Triggered by the Cell method notify_listeners, this method uses a
        tricky shared dictionary technique to propagate updates caused by
        the change of a value to all cells depending on that value.

        Parameters
        ----------
        changed : dict
            A dictionary of cells that have been changed and their previous
            values.

        Returns
        -------
        None
        """
        
        val = self.compute()
        if val != self.value:
            # Updates changed with the current value, if it doesn't already
            # have it.
            changed.setdefault(self, self.value)
            self._value = val
            self.notify_listeners(changed)

    def add_callback(self, callback):
        """
        Adds a callback to this cell's _callbacks set.

        Parameters
        ----------
        callback : ???
            A callback to add.

        Returns
        -------
        None
        """
        
        self._callbacks.add(callback)

    def remove_callback(self, callback):
        """
        Removes a callback from this cell's _callbacks set.

        Parameters
        ----------
        callback : ???
            A callback to remove.

        Returns
        -------
        None
        """
        
        self._callbacks.discard(callback)
        
    def call_callbacks(self):
        """
        Triggers all callbacks with self.value.

        Returns
        -------
        None
        """
        
        for callback in self._callbacks:
            callback(self.value)
    