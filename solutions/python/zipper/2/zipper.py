""" Module solving Zipper exercise for Exercism. """

from functools import partial

VALUE = "value"
LEFT = "left"
RIGHT = "right"

KEYS = (VALUE, LEFT, RIGHT)

class Zipper:
    """
    Class implementing a zipper-type tree representation.
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
        
        return Zipper(tree)
        
    def __init__(self, tree: dict[str: any], parents = None):
        """
        Creates a Zipper object given a tree or subtree and list of parents of
        the Focus node (or None, if the Focus node is the root). Automatically
        generates all required interface functions using setattr and the
        functools partial method.

        Parameters
        ----------
        tree : dict[str: any]
            A dictionary representing a tree. The dictionary has three possible
            keys:
                1: "value": represents the value stored by a node;
                2: "left": the value here is either None (no child nodes) or a
                   dictionary with the same structure describing the sub-tree
                   connected to the left of the root node;
                3: "right": the same as the "left" value except that it is
                   connected to the right of the root node instead of the
                   left.
        parents : list
            A list of parent nodes reaching back up to the root of the tree

        Returns
        -------
        None
        """
        
        self.tree = tree
        self.parents = parents if parents else []
        for key in KEYS:
            setattr(self, f"set_{key}", partial(self.set, key))
            setattr(self, key, partial(self.get, key))

    def get(self, key: str):
        """
        Provides a general framework for "getter" methods that can be frozen
        into a specific variable using the functools "partial" method.

        Parameters
        ----------
        key : str
            A keyword linked to what form the getter should take. The three
            options are:
                1: "value": returns this tree's root value;
                2: "left": returns a new Zipper rooted on left (but tracking
                    the current Zipper through the parents list);
                3: "right": returns a new Zipper rooted on right (but tracking
                   the current Zipper through the parents list).

        Returns
        -------
            The current node's value if key = "value" otherwise the left or
            right subtrees or None if a subtree is requested that does not
            exist.
        """
        
        if key == VALUE:
            return self.tree[VALUE]
        
        output = (Zipper(self.tree[key], 
                         self.parents + [self]) if self.tree[key]
                  else None)
        
        return output
    
    def set(self, key: str, item):
        """
        Provides a general framework for "setter" methods that can be frozen
        into a specific form using the functools "partial" method.

        Parameters
        ----------
        key : str
            A keyword linked to what form the setter should take. The three
            options are:
                1: "value": changes this tree's root value;
                2: "left": changes this tree's left subtree;
                3: "right": changes this tree's right subtree.
        item : any
            The new value for this node (if key = "value") or the new subtree
            for the left or right subtree.

        Returns
        -------
            A new Zipper with the changes as described above.
        """
        
        self.tree[key] = item
        return self.parents[0] if self.parents else self

    def up(self):
        """
        Creates a new Zipper where the Focus is changed to the current
        Focus' parent, or None if the current Focus is the root
        of the tree.

        Returns
        -------
        Zipper
            A new Zipper where the Focus is the current Focus' parent, or None 
            if the current Focus is the root.
        """
        
        return self.parents[-1] if self.parents else None

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
        
        return self.parents[0].tree if self.parents else self.tree
