""" Module solving the DOT DSL Exercism exercise. """

VALID_PRFXS = ("Node", "Edge", "Attribute")
NODE, EDGE, ATTR = VALID_PRFXS
VALID_LENS = {
    NODE: 3,
    EDGE: 4,
    ATTR: 3
}


class Node:
    """ A class representing nodes in a graph. """
    def __init__(self, name, attrs):
        """ Defines a node as a collection of a name and attributes. """
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        """ Checks for the equality of two nodes. """
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    """ A class representing edges in a graph. """
    def __init__(self, src, dst, attrs):
        """ Defines an edge as a source, destination, and attributes. """
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        """ Defines equality of edges in terms of equality of data. """
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data: list[tuple] = None):
        """
        Sets up a graph consisting of nodes, edges, and attributes. Nodes are
        represented as Node objects, edges as Edge objects, and attributes as
        a dictionary of key-value pairs, per the tests.
        
        The main work is validating the data, especially since there are some
        unnatural error handling requirements.

        Parameters
        ----------
        data : list[tuple], optional
            Data to use to initalize the graph. This comes in the form of a
            list of tuples, each tuple beginning with a prefix identifying
            whether the following data is for a node, edge, or attribute. The 
            default is None.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if an undefined prefix is used to label a data item/tuple.
        """
        
        self.nodes = []
        self.edges = []
        self.attrs = {}
        
        if data:
            self._val_data(data)
                    
        if data:
            for item in data:
                try:
                    prefx = item[0]
                except IndexError:
                    raise TypeError("Graph item incomplete")
                else:
                    if prefx == NODE:
                        self.add_node(item)
                    elif prefx == EDGE:
                        self.add_edge(item)
                    elif prefx == ATTR:
                        self.add_attr(item)
                    else:
                        raise ValueError("Unknown item")
                    
    def _val_data(self, data: list[tuple]) -> None:
        """
        Raises an error if input data to the Graph constructor is malformed
        (does not consist of a list of tuples as described above).

        Parameters
        ----------
        data : list[tuple]
            Input data to the Graph constructor.

        Returns
        -------
        None

        Raises
        ------
        TypeError
            Raised if the input data is not a list of tuples.
        """
        
        malformed = False
        
        if isinstance(data, list):
            if isinstance(data[0], tuple):
                pass
            else:
                malformed = True
        else:
            malformed = True
            
        if malformed:
            raise TypeError("Graph data malformed")
                    
    def _val_item(self, data: tuple[str]) -> None:
        """
        Validates individual data items (tuples) when inserting a new item into
        the Graph. Checks whether:
            1: The item actually has any data in it other than the prefix;
            2: The amount of data is precisely that required by the prefix.
        
        Logically, the message "Graph item incomplete" should come up if not
        enough data is present for creating the relevant item, but the tests
        have a case where the error message "Edge is malformed" is required for
        an Edge with only two parameters, so a sensible implementation of the
        checks is impossible.
        
        Note that no validation of the kind of data being provided is done,
        either.

        Parameters
        ----------
        data : tuple[str]
            A tuple providing a data type (Node, Edge, or Attribute) and the
            data which should be used to define an instance of that type.

        Returns
        -------
        None

        Raises
        ------
        TypeError
            Raised if the tuple has only the prefix and no other data.
        ValueError
            Raised if the tuple has a length different than that required by
            the specified data type.
        """
        
        if not data[1:]:
            raise TypeError("Graph item incomplete")
        
        prefx = data[0]
        
        if len(data) != VALID_LENS[prefx]:
            raise ValueError(f"{prefx} is malformed")
                    
    def add_node(self, node_data: tuple) -> None:
        """
        Adds a node to the graph.

        Parameters
        ----------
        node_data : tuple
            Tuple representing the data for the node.

        Returns
        -------
        None
        """
        
        self._val_item(node_data)
        
        node_name, node_attrs = node_data[1:]
        new_node = Node(node_name, node_attrs)
        self.nodes.append(new_node)
        
    def add_edge(self, edge_data: tuple) -> None:
        """
        Adds an edge to the graph.

        Parameters
        ----------
        edge_data : tuple
            Tuple representing the data for the edge.

        Returns
        -------
        None
        """
        
        self._val_item(edge_data)
        
        src, dst, attrs = edge_data[1:]
        new_edge = Edge(src, dst, attrs)
        self.edges.append(new_edge)
        
    def add_attr(self, attr_data: tuple) -> None:
        """
        Adds an attribute to the graph.

        Parameters
        ----------
        attr_data : tuple
            Tuple representing the data for the attribute.

        Returns
        -------
        None
        """
        
        self._val_item(attr_data)
        
        key, value = attr_data[1:]
        self.attrs[key] = value
