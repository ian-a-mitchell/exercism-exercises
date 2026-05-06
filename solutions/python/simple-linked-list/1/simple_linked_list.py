""" Module for solving Simple Linked List exercise on Exercism. """

class EmptyListException(Exception):
    """ Custom exception for empty linked list. """
    
    def __init__(self: Exception, message: str):
        """
        Creates exception for empty linked list with custom message.
        """
        self.message = message


class Node:
    """ Represents a node in a simply linked list. """
    def __init__(self, value):
        """
        Sets up new Node object given a value to store.

        Parameters
        ----------
        value : obj
            Any object whatsoever.

        Returns
        -------
        None
        """
        self.my_value = value
        self.next_node = None

    def value(self):
        """ Simply a getter for the Node's value. """
        
        return self.my_value
    
    def add_node(self, next_node):
        """
        Changes the next_node parameter to contain a different next_node.

        Parameters
        ----------
        next_node : Node
            The next node that this one should link to.

        Returns
        -------
        None
        """
        
        self.next_node = next_node

    def next(self):
        """
        See below.

        Returns
        -------
        Node
            The next node in the sequence, or None if none has been set.
        """
        
        return self.next_node


class LinkedList:
    """ Class implementing a one-directional linked list. """
    def __init__(self, values=None):
        """
        Sets up linked list given a list of values. Per tests, the head will
        be the final value in the list of values.

        Parameters
        ----------
        values : list, optional
            A list of values to store in the linked list. The default is None.

        Returns
        -------
        None
        """
                
        self.my_head = None
        self.length = 0
        
        if values:
            for value in values:
                self.push(value)

    def __iter__(self):
        """ Turns the linked list into an iterable. """
        
        cur_node = self.my_head
        while cur_node:
            yield cur_node.value()
            cur_node = cur_node.next()

    def __len__(self):
        """ Wrapper for the length parameter. """
                
        return self.length

    def head(self):
        """ 
        Returns the current head of the linked list, or raises an empty length
        error if there is none.
        """
        
        if not self.my_head:
            raise EmptyListException("The list is empty.")
        
        return self.my_head

    def push(self, value):
        """ 
        Adds a new value to the list and sets the node to be the new head.
        """
        
        new_head = Node(value)
        new_head.add_node(self.my_head)
        self.my_head = new_head
        self.length += 1

    def pop(self):
        """
        Returns the value of the head node and removes it from the list.

        Returns
        -------
        Obj
            Whatever the value in the head node is.

        Raises
        ------
        EmptyListException
            Raised if the list is empty.
        """
        
        if not self.my_head:
            raise EmptyListException("The list is empty.")
        
        output = self.my_head.value()
        self.my_head = self.my_head.next()
        self.length -= 1
        
        return output

    def reversed(self):
        """
        Returns a new linked list that runs in the opposite direction.
        """
        
        new_list = LinkedList()
        cur_node = self.my_head
        
        while cur_node:
            new_list.push(cur_node.value())
            cur_node = cur_node.next()
        
        return new_list