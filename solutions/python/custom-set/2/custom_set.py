""" 
Module implementing a set iterable for the Exercism Custom Set exercise.
"""

class CustomSet:
    """ Class providing set-like storage for arbitrary data. """
    def __init__(self, elements: iter = None) -> None:
        """
        Creates a set given an optional initalizing iterable of elements. If
        no initializing iterable is provided, creates an empty set.

        Parameters
        ----------
        elements : iterable, optional
            An iterable containing data to store in the set. The default is [].

        Returns
        -------
        None
        """
        
        self.elements = []
        self.idx = 0
        if elements:
            for element in elements:
                self.add(element)
                
    def isempty(self) -> bool:
        """ Returns true if the set is empty, false otherwise. """
        
        return not self.elements

    def __contains__(self, element) -> bool:
        """ Returns true if the element is in this set, false otherwise. """
        
        return element in self.elements
    
    def __str__(self) -> str:
        """ Provides a string representation of the set. """
        
        return f"Stored elements: {self.elements}"

    def __eq__(self, other) -> bool:
        """
        Checks for equality between two sets. Sets are equal iff they are
        mutual subsets, therefore it suffices to check that both are subsets
        of each other.

        Parameters
        ----------
        other : CustomSet
            The set to check .

        Returns
        -------
        bool
            True if the sets are equal, false otherwise.
        """
                
        return self.issubset(other) and other.issubset(self)
    
    def __hash__(self):
        """ A hash method, needed by the linter. """
        
        return hash(tuple(self.elements))
    
    def __sub__(self, other):
        """
        Subtracts other from self and returns the result. Subtracting set B
        from Set A means creating a new set that contains all elements of set
        A that are not in set B, or in other words finding the subset of A
        that excludes all elements in the intersection of A and B.

        Parameters
        ----------
        other : CustomSet
            The set whose elements should be removed from the output set.

        Returns
        -------
        CustomSet
            The subset of self which is disjoint with the set other.
        """
        
        remove_elements = self.intersection(other)
        
        new_elements = [element for element in self.elements
                        if element not in remove_elements]
                
        return CustomSet(new_elements)

    def __add__(self, other):
        """
        Adds self and other, that is, takes the union of them.

        Parameters
        ----------
        other : CustomSet
            The set whose elements should be added to self to form the output
            set.

        Returns
        -------
        CustomSet
            A set containing all elements from self and other.
        """
        
        new_set = CustomSet(elements = self.elements)
        
        for element in other.elements:
            new_set.add(element)
            
        return new_set

    def issubset(self, other) -> bool:
        """
        Determines whether self is a subset of other. Set A is a subset of set
        B if and only if every element of set A is an element of set B.
        
        This algorithm takes advantage of the fact that Python represents True
        as +1 and False as 0. Replacing the sequence of elements in self with a
        sequence of booleans, each representing whether that element is found
        in other, means that the sum will be equal to the number of elements
        found in other. If that number is equal to the length, it means that
        every element from self is found in other, which is the definition of
        a subset.

        Parameters
        ----------
        other : CustomSet
            The set which this set may or may not be a subset of.

        Returns
        -------
        bool
            True if self is a subset of other, false otherwise.
        """
        
        in_other = sum((element in other for element in self.elements))
                
        return in_other == len(self.elements)

    def isdisjoint(self, other) -> bool:
        """
        Determines whether self is disjoint from other. Set A being disjoint
        from Set B means that A has no elements that are found in B.
        
        The same method as above is used, except that the sum of the sequence
        of booleans should be 0 if self and other are disjoint

        Parameters
        ----------
        other : CustomSet
            The set which this one may or may not be disjoint from.

        Returns
        -------
        bool
            True if self and other are disjoint, false otherwise.
        """
        
        in_other = sum((element in other for element in self.elements))
                    
        return in_other == 0

    def add(self, element) -> None:
        """
        Adds an element to self. The only complication is doing nothing if it
        is already in self.

        Parameters
        ----------
        element : TYPE
            Arbitrary element to add to self.

        Returns
        -------
        None
        """
        
        if element not in self:
            self.elements.append(element)

    def intersection(self, other):
        """
        Finds the intersection of self and other. The intersection of sets A
        and B is equivalent to the set of all elements of A that are in B, or
        vice versa.

        Parameters
        ----------
        other : CustomSet
            The set to calculate the intersection with.

        Returns
        -------
        CustomSet
            A set containing all and only elements that are found in self and
            other.
        """
        
        intersect_data = [element for element in self.elements
                          if element in other]
                
        return CustomSet(intersect_data)