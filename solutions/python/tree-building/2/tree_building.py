""" Module solving Tree Building exercise on Exercism. """

class Record:
    """ Class defining a record stored in an unorganized list. """
    def __init__(self, record_id, parent_id):
        """ 
        Record is defined by the id of itself and its parent (for building the 
        tree itself when necessary).
        """
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    """ Class defining a node in a tree. """
    def __init__(self, node_id):
        """
        Node is defined by its own id and a list of child nodes.
        """
        self.node_id = node_id
        self.children = []
        
_ER_MESSAGES = {
    "invalid": "Record id is invalid or out of order.",
    "root": "Only root should have equal record and parent id.",
    "wrong_parent": "Node parent_id should be smaller than its record_id."
}

def invalidate_tree(records) -> str:
    """
    Function to check whether a list of records forms a valid tree. A valid
    tree is defined by three criteria:
        1: There is a node for every record_id between 0 (the root entry) and
           whatever the maximum record_id is; no record ids can be skipped.
        2: No node but the root has itself as its parent.
        3: No node can list a record_id larger than its own as its parent
           (this includes the root node, which together implies that the root
            always has parent itself)

    Parameters
    ----------
    records : Record
        A list of records. It is assumed to be sorted as this function is only
        called after it is, in fact, sorted.

    Returns
    -------
    str
        A code for the error message to raise, or the empty string if there is
        no error to raise.
    """
    
    output = ""
    
    if [record.record_id for record in records] != list(range(len(records))):
        output = "invalid"
    
    for record in records:
        if record.parent_id >= record.record_id:
            if record.record_id != 0 and record.parent_id == record.record_id:
                output = "root"
            elif record.record_id != 0 or record.parent_id > record.record_id:
                output = "wrong_parent"
                
    return output
                    
def BuildTree(records):
    """
    Given a list of Records, ensures that they form a valid tree and then
    builds that tree. The tree is represented by the Node object for the root
    of the tree.

    Parameters
    ----------
    records : Record
        The unordered records to be validated and turned into a tree.

    Returns
    -------
    root : Node
        The root node of the tree corresponding to the provided records.

    Raises
    ------
    ValueError
        Error raised given the criteria listed above in "invalidate_tree".
    """
    
    root = None
    
    if not records:
        return root
    
    records.sort(key=lambda record: record.record_id)
    
    invalidity = invalidate_tree(records)
    
    if invalidity:
        raise ValueError(_ER_MESSAGES[invalidity])
    
    nodes = {record.record_id:Node(record.record_id) for record in records}
    
    for record in records:
        if record.record_id != 0:
            nodes[record.parent_id].children.append(nodes[record.record_id])
    
    root = nodes[0]
        
    return root
