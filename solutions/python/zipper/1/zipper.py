""" Module solving Zipper exercise for Exercism. """

VALUE = "value"
LEFT = "left"
RIGHT = "right"

class Node:
    """ Helper class to act as nodes in a tree."""
    
    def __init__(self, tree: dict[str: any]):
        """
        Given a tree in the form of a dictionary with string keys, sets up a
        tree in the form of Node objects containing other Node objects.
        Operates recursively using the "left" and "right" keywords, that is, 
        the input is used to set up a root Node and then "left" and "right"
        Nodes using the relevant subdictionary, as if those Nodes were
        themselves root nodes.

        Parameters
        ----------
        tree : dict[str: any]
            A dictionary representing a tree. The dictionary has three possible
            keys:
                1: "value": represents the value stored by the Node;
                2: "left": the value here is either None (no child nodes) or a
                   dictionary with the same structure describing the sub-tree
                   connected to the left of the root node;
                3: "right": the same as the "left" value except that it is
                   connected to the right of the root node instead of the
                   left.

        Returns
        -------
        None
        """
        
        self._value = tree[VALUE]
        self.set_left(tree[LEFT])
        self.set_right(tree[RIGHT])
        
    def __eq__(self, other) -> bool:
        """
        Checks equality of self with other. The main trick is returning False
        when other is None. Equality is defined as trees having the same value
        in the root node and identical left and right subtrees.

        Parameters
        ----------
        other : Node
            The other node to compare this one to.

        Returns
        -------
        bool
            True if the two trees are equal, False otherwise.
        """
        
        if other:
            same_value = self._value == other.value
            same_left = self._left == other.left
            same_right = self._right == other.right
        
            return same_value and same_left and same_right
        
        # handles case where other is None
        return False
    
    def __hash__(self):
        """ Defines a hash value to satisfy the linter. """
        
        return hash(self._value)
    
    def __str__(self):
        """
        Provides a string representation based on the dictionary used to
        originally define the tree.
        """
        
        return str(self.to_dict())
        
    def set_left(self, tree: dict[str: any]):
        """
        Redefines this node's left subtree using the provided dictionary-based
        tree definition.

        Parameters
        ----------
        tree : dict[str: any]
            A dictionary identical to the one used to define a Node meant to
            describe a new left subtree.

        Returns
        -------
        None
        """
                
        self._left = Node(tree) if tree else None
        
    def set_right(self, tree: dict[str: any]):
        """
        Redefines this node's right subtree using the provided dictionary-based
        tree definition.

        Parameters
        ----------
        tree : dict[str: any]
            A dictionary identical to the one used to define a Node meant to
            describe a new right subtree.

        Returns
        -------
        None
        """
                
        self._right = Node(tree) if tree else None
        
    def set_value(self, new_value: any):
        """
        Changes the value of this Node.

        Parameters
        ----------
        new_value : any
            The new value for this node to store.

        Returns
        -------
        None
        """
        
        self._value = new_value
        
    def to_dict(self) -> dict:
        """
        Converts this Node and its subtrees into a dictionary of dictionaries
        identical to the one used to originally define it.

        Returns
        -------
        dict
            A dictionary representing a tree. The dictionary has three possible
            keys:
                1: "value": represents the value stored by the Node;
                2: "left": the value here is either None (no child nodes) or a
                   dictionary with the same structure describing the sub-tree
                   connected to the left of the root node;
                3: "right": the same as the "left" value except that it is
                   connected to the right of the root node instead of the
                   left.
        """
        
        output = {
            VALUE: self._value,
            LEFT: self._left.to_dict() if self._left else None,
            RIGHT: self._right.to_dict() if self._right else None
        }
        
        return output
    
    def find_parent(self, other):
        """
        The trickiest function. Given a Node other, returns the parent Node
        to other if other is found in the tree. Operates by checking whether
        other is a child of this node, in which case it returns itself;
        otherwise, it asks whichever children exist whether it's a child of
        them or their children.
        
        If no parent is found (which in practice should not happen), it returns 
        None, otherwise it returns whichever parent is found. Note that it 
        prefers the left branch if identical copies of other exist in both left 
        and right.

        Parameters
        ----------
        other : Node
            The Node whose parent is sought.

        Returns
        -------
        Node
            The Node representing the parent of other, that is, the Node
            containing other as either its _left or _right value.
        """
        
        output = None
        
        if self._left or self._right:
            if self._left and self._left == other:
                output = self
            elif self._right and self._right == other:
                output = self
            
            if not output:
                left_par = self._left.find_parent(other) if self._left else None
                right_par = self._right.find_parent(other) if self._right else None
                
                if left_par:
                    output = left_par
                elif right_par:
                    output = right_par
                
        return output
    
    @property
    def left(self):
        """ Returns the left subtree. """
        
        return self._left
    
    @property
    def right(self):
        """ Returns the right subtree. """
        
        return self._right
    
    @property
    def value(self):
        """ Returns this Node's value. """
        
        return self._value

class Zipper:
    """
    Class implementing a Zipper-like tree representation (rather fakely).
    """
    
    @staticmethod
    def from_tree(tree: dict[str: any]):
        """
        Given an input tree representation, creates a new Zipper from it.

        Parameters
        ----------
        tree : dict[str: any]
            A dictionary representing a tree. The dictionary has three possible
            keys:
                1: "value": represents the value stored by the Node;
                2: "left": the value here is either None (no child nodes) or a
                   dictionary with the same structure describing the sub-tree
                   connected to the left of the root node;
                3: "right": the same as the "left" value except that it is
                   connected to the right of the root node instead of the
                   left.

        Returns
        -------
        Zipper
            A Zipper with the root node of the supplied tree dictionary as the
            head and as the focus.
        """
        
        head = Node(tree)
        
        return Zipper(head, head)
        
    def __init__(self, head: Node, focus: Node):
        """
        Actually creates a Zipper object given a head Node and focus Node.

        Parameters
        ----------
        head : Node
            A Node containing the full tree.
        focus : Node
            A Node representing the current Focus for the tree, that is, the
            Node which access and manipulation functions assume is the "home
            base".

        Returns
        -------
        None
        """
        
        self._head = head
        self._focus = focus

    def value(self):
        """
        Returns the value of the Focus Node.

        Returns
        -------
        any
            The value of the Focus Node.
        """
        
        return self._focus.value

    def set_value(self, new_value):
        """
        Creates a new Zipper with a different value for the Focus Node.

        Parameters
        ----------
        new_value : any
            The new value for the Focus Node.

        Returns
        -------
        Zipper
            A new Zipper with the value of the Focus Node changed to new_value.
        """
        
        self._focus.set_value(new_value)
        
        return Zipper(self._head, self._focus)

    def left(self):
        """
        Creates a new Zipper with the Focus Node changed to the current Focus
        Node's _left value, or None if that value is None.

        Returns
        -------
        Zipper
            A new Zipper with the Focus Node changed to the current Focus
            Node's _left value or None if that value is None.
        """
        
        self._focus = self._focus.left
        
        if self._focus:
            return Zipper(self._head, self._focus)
        
        return None

    def set_left(self, new_left: dict[str: any]):
        """
        Given a subtree definition, returns a new Zipper where the current
        Focus Node's _left value now consists of that new subtree.

        Parameters
        ----------
        new_left : dict[str: any]
            A dictionary containing the definition of a new left subtree.

        Returns
        -------
        Zipper
            A new Zipper where the Focus Node's _left value consists of the
            new subtree defined in new_left.
        """
        
        self._focus.set_left(new_left)
        
        return Zipper(self._head, self._focus)

    def right(self):
        """
        Creates a new Zipper with the Focus Node changed to the current Focus
        Node's _right value, or None if that value is None.

        Returns
        -------
        Zipper
            A new Zipper with the Focus Node changed to the current Focus
            Node's _right value or None if that value is None.
        """
        
        self._focus = self._focus.right
        
        if self._focus:
            return Zipper(self._head, self._focus)
        
        return None

    def set_right(self, new_right: dict[str: any]):
        """
        Given a subtree definition, returns a new Zipper where the current
        Focus Node's _right value now consists of that new subtree.

        Parameters
        ----------
        new_right : dict[str: any]
            A dictionary containing the definition of a new right subtree.

        Returns
        -------
        Zipper
            A new Zipper where the Focus Node's _right value consists of the
            new subtree defined in new_right.
        """
        
        self._focus.set_right(new_right)
        
        return Zipper(self._head, self._focus)

    def up(self):
        """
        Creates a new Zipper where the Focus Node is changed to the current
        Focus Node's parent node, or None if the current Focus Node is the root
        of the tree.

        Returns
        -------
        Zipper
            A new Zipper where the Focus Node is the current Focus Node's
            parent Node, or None if the current Focus Node is the root Node.
        """
        
        if self._focus == self._head:
            return None
        
        self._focus = self._head.find_parent(self._focus)
        
        return Zipper(self._head, self._focus)

    def to_tree(self) -> dict:
        """
        Provides a dictionary-based representation of the whole tree.

        Returns
        -------
        dict
            A dictionary representing a tree. The dictionary has three possible
            keys:
                1: "value": represents the value stored by the Node;
                2: "left": the value here is either None (no child nodes) or a
                   dictionary with the same structure describing the sub-tree
                   connected to the left of the root node;
                3: "right": the same as the "left" value except that it is
                   connected to the right of the root node instead of the
                   left.
        """
        
        return self._head.to_dict()
