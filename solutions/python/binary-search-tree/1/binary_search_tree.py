""" Module solving the Binary Search Tree exercise for Exercism. """

class TreeNode:
    """ Class representing a node in a binary tree """
    def __init__(self, data, left=None, right=None):
        """
        Initializes a node for a binary tree with data.

        Parameters
        ----------
        data : TYPE
            Data to store (arbitrary type).
        left : TreeNode, optional
            The node to the left (less than or equal to). The default is None.
        right : TYPE, optional
            The node to the right (greater than). The default is None.
            
        In practice I do not actually use the left or right parameters...

        Returns
        -------
        None
        """
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        """ String representation of this node. """
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'
    
    def insert_data(self, data) -> None:
        """
        Inserts a new data point into the tree formed by this node and its
        children nodes. Recursively finds the correct point to insert the data
        by walking the tree to the first node with an empty leaf node with the
        right relationship to the data.

        Parameters
        ----------
        data : TYPE
            Data to add to the tree.

        Returns
        -------
        None
        """
        
        if data > self.data:
            if self.right:
                self.right.insert_data(data)
            else:
                self.right = TreeNode(data)
        else:
            if self.left:
                self.left.insert_data(data)
            else:
                self.left = TreeNode(data)
    
    def sorted_data(self) -> list:
        """
        Creates a sorted representation of the tree formed by this node and its
        children. Since it's a binary tree it's already sorted if you walk it
        correctly. This is done recursively like with inserting data.

        Returns
        -------
        list
            List of the data in the nodes.
        """
        
        output = [self.data]
        
        if self.left or self.right:
            sorted_left = []
            sorted_right = []
            if self.left:
                sorted_left = self.left.sorted_data()
            if self.right:
                sorted_right = self.right.sorted_data()
                
            output = sorted_left + output + sorted_right
            
        return output


class BinarySearchTree:
    """
    Class representing a binary search tree. Not really needed since the tree
    nodes already implicitly form a tree.
    """
    
    def __init__(self, tree_data: list[str]):
        """
        Sets up binary search tree.

        Parameters
        ----------
        tree_data : list[str]
            The data to store in the tree. Implicitly already sorted.

        Returns
        -------
        None
        """
        
        self.root = TreeNode(tree_data.pop(0))
        
        while tree_data:
            self.root.insert_data(tree_data.pop(0))

    def data(self):
        """ Wraps the node's representation of the tree. """
        
        return self.root

    def sorted_data(self):
        """
        Acts as a wrapper for the nodal function for providing a sorted
        representation of the data stored in the tree.
        """
        
        return self.root.sorted_data()