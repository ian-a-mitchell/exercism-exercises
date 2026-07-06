""" Module solving the Satellite exercise on Exercism. """

def validate_tree_input(preorder: list, inorder: list) -> None:
    """
    Validates that the preorder and inorder lists can be used to generate a
    binary tree. This is possible if:
        1: They have the same number of elements;
        2: They have the same elements (possibly in a different order);
        3: Neither has any repeated elements, that is, all elements are
           unique and appear only once in each list.
           
    A ValueError with a specified error message is raised if any of these
    conditions is not met.

    Parameters
    ----------
    preorder : list
        A list of values for a binary tree in pre-order ordering. This starts
        with the value of the root node, then contains the pre-order structure
        of the left subtree, then the pre-order structure of the right subtree.
    inorder : list
        A list of values for a binary tree in in-order ordering. This starts
        with the leftmost node, then proceeds rightwards until reaching the
        rightmost node.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        Raised when any of the three above conditions are not met.
    """
    
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
        
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
        
    if len(set(preorder)) != len(preorder) or len(set(inorder)) != len(inorder):
        raise ValueError("traversals must contain unique items")
        
def find_left_right_lists(preorder: list, inorder: list):
    """
    Given a list of binary tree values in pre-order and in-order orderings,
    finds sublists that correspond to the pre-order and in-order orderings of
    the left and right sublists.

    Parameters
    ----------
    preorder : list
        A list of values for a binary tree in pre-order ordering. This starts
        with the value of the root node, then contains the pre-order structure
        of the left subtree, then the pre-order structure of the right subtree.
    inorder : list
        A list of values for a binary tree in in-order ordering. This starts
        with the leftmost node, then proceeds rightwards until reaching the
        rightmost node.

    Returns
    -------
    l_preorder : TYPE
        The values of the left subtree in pre-order ordering.
    l_inorder : TYPE
        The values of the left subtree in in-order ordering.
    r_preorder : TYPE
        The values of the right subtree in pre-order ordering.
    r_inorder : TYPE
        The values of the right subtree in in-order ordering.
    """
    
    root_value = preorder[0]
    center = inorder.index(root_value)
    
    # The in-order list is easy to split since the root node is in the middle
    l_inorder = inorder[0:center]
    r_inorder = inorder[center + 1:]
    
    l_preorder = []
    l_stop = 1
    
    # Find the sublist of the preorder list that has the same elements as
    # the left inorder list.
    while l_stop < len(preorder) and set(l_preorder) != set(l_inorder):
        l_stop += 1
        l_preorder = preorder[1:l_stop]
        
    # Since the zeroth element of the preorder list is the root node and the
    # left subtree comes first, anything left after the left subtree is
    # found must be the right preorder list.
    r_preorder = preorder[l_stop:]
    
    return (l_preorder, l_inorder, r_preorder, r_inorder)

def tree_from_traversals(preorder: list, inorder: list) -> dict:
    """
    Given a list of binary tree values in pre-order form and a list in in-order
    form, rebuild the tree. Use a recursive algorithm where the root node is
    populated and then the left and right subtrees are built and appended using
    the sections of the preorder and inorder lists corresponding to them. The
    base case is if the preorder and inorder lists only contain one item, that
    is, the root node.
    
    Also handles the case of empty lists (an empty dictionary is returned) and
    calls a validator to make sure that the provided lists can be reconstructed
    into a tree correctly.

    Parameters
    ----------
    preorder : list
        A list of values for a binary tree in pre-order ordering. This starts
        with the value of the root node, then contains the pre-order structure
        of the left subtree, then the pre-order structure of the right subtree.
    inorder : list
        A list of values for a binary tree in in-order ordering. This starts
        with the leftmost node, then proceeds rightwards until reaching the
        rightmost node.

    Returns
    -------
    dict
        Dictionary describing a binary tree. Has three valid keys:
            "v": The stored value of this node;
            "l": A dictionary containing the left subtree;
            "r": A dictionary containing the right subtree;
        It is recursive, that is, "l" and "r" are also dictionaries with this
        structure to them.
    """
    
    validate_tree_input(preorder, inorder)
    
    output = {}
    
    if preorder and inorder:
        output["v"] = preorder[0]
        
        if len(preorder) != 1:
            split_lists = find_left_right_lists(preorder, inorder)
            
            l_preorder, l_inorder, r_preorder, r_inorder = split_lists
            
            output["l"] = tree_from_traversals(l_preorder, l_inorder)
            output["r"] = tree_from_traversals(r_preorder, r_inorder)
        else: # base case: no subtrees
            output["l"] = {}
            output["r"] = {}
        
    return output
