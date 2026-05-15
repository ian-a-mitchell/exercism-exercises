""" 
Module implementing a doubly linked list for the Exercism exercise Linked List.
"""

class Node:
    """ Class implementing a linked list node. """
    def __init__(self, value, succeeding=None, previous=None):
        """
        Creates a new node for a doubly linked list.

        Parameters
        ----------
        value : TYPE
            Arbitrary value for the node to store.
        succeeding : Node, optional
            The next node in the linked list. The default is None.
        previous : TYPE, optional
            The previous node in the linked list. The default is None.

        Returns
        -------
        None
        """
        
        self.value = value
        self.next = succeeding
        self.prev = previous
        
    def set_next(self, succeeding):
        """
        Replaces the current next node of this node with a different node.

        Parameters
        ----------
        succeeding : Node
            The new node that this node should list as its next node.

        Returns
        -------
        None
        """
        
        self.next = succeeding
        
    def set_prev(self, previous):
        """
        Replaces the current previous node of this node with a different node.

        Parameters
        ----------
        previous : Node
            The new node that this node should list as its next node.

        Returns
        -------
        None
        """
        
        self.prev = previous


class LinkedList:
    """ A class implementing a doubly linked list. """
    
    def __init__(self):
        """
        Creates a doubly linked list object with no parameters.
        
        Separate head and tail values are used to allow O(1) access to the
        first and final elements of the list, respectively.

        Returns
        -------
        None
        """
        
        self.head = None
        self.tail = None
        self.length = 0
        
    def __len__(self) -> int:
        """
        Returns the stored length of the list.

        Returns
        -------
        int
            Number of nodes in the list, counting from one.
        """
        
        return self.length

    def push(self, value):
        """
        Inserts a new node at the end of the list.

        Parameters
        ----------
        value : TYPE
            Value that the new node should store.

        Returns
        -------
        None
        """
        
        self._insert_node(Node(value, previous = self.tail))
        
    def unshift(self, value):
        """
        Inserts a new node at the beginning of the list.

        Parameters
        ----------
        value : TYPE
            Value that the new node should store.

        Returns
        -------
        None
        """
            
        self._insert_node(Node(value, succeeding = self.head))
        
    def _insert_node(self, node: Node):
        """
        Inserts a new node, determining whether to add it at the beginning or
        end based on whether the previous or next nodes are set.

        Parameters
        ----------
        node : Node
            A node to insert into the list.

        Returns
        -------
        None
        """
        
        if not (node.next or node.prev):
            self.head = node
            self.tail = node
        elif node.prev:
            node.prev.set_next(node)
            self.tail = node
        elif node.next:
            node.next.set_prev(node)
            self.head = node
            
        self.length += 1
            
    def pop(self):
        """
        Removes the final element from the list and returns the stored value.

        Returns
        -------
        TYPE
            The value stored by the final node in the list.
        """
        
        return self._return_node(self.tail)
    
    def shift(self):
        """
        Removes the first element from the list and returns the stored value.

        Returns
        -------
        TYPE
            The value stored by the first node in the list.
        """
        
        return self._return_node(self.head)
    
    def _return_node(self, node: Node):
        """
        Helper function for the pop and shift methods to reduce code
        duplication.

        Parameters
        ----------
        node : Node
            The node whose value should be returned, either the head or tail.

        Returns
        -------
        TYPE
            The value stored in Node node.

        Raises
        ------
        IndexError
            Raised if the list is empty (node is None).
        """
        
        if not node:
            raise IndexError("List is empty")
        
        if self.head == self.tail:
            self.tail = None
            self.head = None
        elif node == self.tail:
            prev_node = node.prev
            prev_node.set_next(None)
            self.tail = prev_node
        elif node == self.head:
            next_node = node.next
            next_node.set_prev(None)
            self.head = next_node
            
        self.length -= 1
            
        return node.value
        
    def delete(self, value):
        """
        Removes the first node with the specified value from the list. Never
        removes more than one node.

        Parameters
        ----------
        value : TYPE
            The value to search for and remove.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if the value is not in the list.
        """
        
        curr_node = self.head
        
        while curr_node:
            if curr_node.value == value:
                break
            curr_node = curr_node.next
        else:
            # The only way we got here was if self.head was None or the value
            # wasn't found in the list, which per tests are error conditions.
            raise ValueError("Value not found")
            
        prev_node = curr_node.prev
        next_node = curr_node.next
        
        if prev_node:
            prev_node.set_next(next_node)
        else:
            self.head = next_node
        
        if next_node:
            next_node.set_prev(prev_node)
        else:
            self.tail = prev_node
            
        self.length -= 1