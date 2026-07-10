""" Module solving the POV exercise from Exercism. """

from json import dumps

class Tree:
    """ Class implementing a data tree. Dime a dozen. """
    
    def __init__(self, label, children=None):
        """ Constructor method set up by Exercism. """
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        """ Creates representation of Tree as dictionary. """
        return {self.label: [child.__dict__() 
                             for child in sorted(self.children)]}

    def __str__(self, indent=None):
        """ Creates string representation of the self using JSON. """
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        """ Defines a less than comparison. Not sure why... """
        return self.label < other.label

    def __eq__(self, other):
        """ Defines the equality of two Tree objects. """
        return self.__dict__() == other.__dict__()
    
    def __hash__(self):
        """ Defines a hash value to suppress a linter complaint. """
        return hash(self.label)
    
    def get_path(self, destination: str) -> list:
        """
        Creates a list of tree objects tracing the path between self and a
        Tree with label destination, or None if no such path is found. Uses
        depth-first recursive search where it checks itself, then asks its 
        children if they can find a path and if they can appends itself to the
        start of the path before returning, and finally gives up.
        
        Essential helper method for from_pov and path_to.

        Parameters
        ----------
        destination : str
            The label of a Tree to find a path to.

        Returns
        -------
        list[Tree]
            A list of trees proceeding from self deeper into the tree until it
            reaches a node with label destination.
        """
        
        if destination == self.label:
            return [self]
        
        for child in self.children:
            path = child.get_path(destination)
            if path:
                return [self] + path
        
        return None

    def from_pov(self, source: str):
        """
        Creates a new tree with the parent being the node with the label
        source. Algorithmically, gets the path from this node (assumed to be
        the root) to the source node, then progresses through the list and
        moves the leading (parent) node to be a child of the next (child) node
        except without the child node as one of its children.

        Parameters
        ----------
        source : str
            The label of the node to reparent on.

        Returns
        -------
        Tree
            Tree represented with source as the root node.

        Raises
        ------
        ValueError
            Raised if _get_path cannot find a path from self to source, which
            only happens if source cannot be found in the tree.
        """
        
        work_queue = self.get_path(source)
        
        if not work_queue:
            raise ValueError("Tree could not be reoriented")
                    
        while len(work_queue) > 1:
            parent = work_queue.pop(0)
            child = work_queue[0]
            parent.children.remove(child)
            child.children.append(parent)
            work_queue[0] = child
            
        if len(work_queue) == 1:
            return work_queue.pop()

    def path_to(self, source: str, destination: str) -> list[str]:
        """
        Provides user with a list of nodes on the path between the nodes
        labeled "source" and "destination". Works by reparenting the tree on
        the source node, getting the path from the source to the destination
        node, and then building a list out of the labels of each tree object
        in the path list.

        Parameters
        ----------
        source : str
            String label for the source node.
        destination : str
            String label for the destination node.

        Returns
        -------
        list[str]
            List of strings, each string being the label of a node. The first
            string in the list is source, the last is destination, the others
            are the labels of nodes on the path between them.

        Raises
        ------
        ValueError
            Raised if no path can be found between source and destination. In
            practice, this means destination is not in the tree.
        """
        
        reorient = self.from_pov(source)
        path = reorient.get_path(destination)
        
        if not path:
            raise ValueError("No path found")
        
        return [next_tree.label for next_tree in path]
