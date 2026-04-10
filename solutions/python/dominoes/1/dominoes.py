""" Set of methods for solving the Dominoes problem on Exercism

The basic method is to generate and test candidate solutions, and if validated
to immediately return the candidate.
"""

import copy

def valid_domino_chain(can: list[tuple]) -> bool:
    """
    Checks whether a candidate solution forms a valid domino chain. A valid
    domino chain has the qualities:
        1: The final numerical value on each domino (in each tuple) matches the
           first numerical value on the next domino, e.g. (3, 1) <-> (1, 2)
        2: The first numerical value on the first stone matches the final
           numerical value on the final stone, e.g. (1, 2)...(5, 1)

    Parameters
    ----------
    can : list[tuple]
        A candidate solution, consisting of a list of dominoes (tuples) ordered
        solution-wise, with the first value of the first tuple representing
        its first numerical value, etc.

    Returns
    -------
    bool
        True if the chain is valid, false otherwise.
    """
    
    output = True
    
    for idx, domino in enumerate(can):
        if output:
            if idx < len(can) - 1:
                if domino[-1] != can[idx + 1][0]:
                    output = False
                    
    if output and can[0][0] != can [-1][-1]:
        output = False
            
    return output

def build_sub_chains(head: tuple, dominoes: list[tuple]) -> list[list]:
    """
    The core of the algorithm. A method to build all possible chains beginning
    with the specified ("head") domino with the specified dominoes. Proceeds
    recursively:
        1: The base case is having two dominoes (the head and one other). There
           are three possible options:
               1: The other domino's first value matches the final value of the
                  head domino. In this case, the chain is [[head, other]]
               2: The other domino's final value matches the final value of the
                  head domino. In this case, the other domino must be rotated,
                  and the resulting chain is [[head, r_other]]
               3: Neither value on the other domino matches the final value of
                  the head. No valid chain can be found, so the empty list is
                  returned.
        2: The other case is having more than two dominoes (the case of one
           domino is handled separately). In this case, the logic proceeds as:
            1: All available dominoes that match the head's final value on 
               either side are identified.
            2: If there are none, there is no valid chain, so the empty list is
               returned as before.
            3: If there are some, the list of candidate next dominoes is looped
               over.
            4: If necessary, the candidate next domino is rotated to match the 
               current head correctly.
            5: A list of the remaining dominoes once the candidate next domino
               is removed is created. Note the deep copy, which avoids editing
               the original list of dominoes.
            6: This method is called again to create the list of all possible
               chains starting with the candidate next domino.
            7: If there are any possible chains, each of the candidate chains
               is re-headed with the current head and appended to the output.
            8: Otherwise, process starts over with 4 for the next candidate for
               the next domino in the chain, after the current head.
            9: Once all candidate next dominoes have been checked and their
               candidate chains (if any) have been appended to the output,
               everything falls through and whatever is in the output is
               returned.
               
    Note that the empty list is returned if no subchains using all of the
    dominoes can be found, or if a two-domino chain cannot be formed.

    Parameters
    ----------
    head : tuple
        A tuple corresponding to the first domino in the current chain or
        subchain.
    dominoes : list[tuple]
        A list of tuples, each of which corresponds to one available domino
        other than the head.

    Returns
    -------
    list[list]
        A list of lists, each sublist containing a possible valid chain of
        dominoes beginning with the head and containing all of the dominoes
        in dominoes.
    """
    
    output = []
    
    if len(dominoes) == 1:
        if dominoes[0][-1] == head[-1]:
            output = [[head, dominoes[0][::-1]]]
        elif dominoes[0][0] == head[-1]:
            output = [[head, dominoes[0]]]
    else:
        can_next = []
        
        for domino in dominoes:
            if domino[0] == head[-1] or domino[-1] == head[-1]:
                can_next.append(domino)
                                
        if not can_next:
            return output
        
        for can_head in can_next:
            
            true_can = can_head
            if true_can[-1] == head[-1]:
                true_can = true_can[::-1]
            rem_dominoes = copy.deepcopy(dominoes)
            rem_dominoes.remove(can_head)
            
            can_chain = build_sub_chains(true_can, rem_dominoes)
            
            if can_chain:
                for chain in can_chain:
                    candidate = [head]
                    candidate.extend(chain)
                    output.append(candidate)
                            
    return output

def can_chain(dominoes: list[tuple]) -> list[tuple]:
    """
    Method to build and validate a chain of dominoes following the spec for the
    Exercism "Dominoes" exercise.
    
    Handles the cases of
        1: An empty list of dominoes
        2: A single domino
        
    Seperately from the method "build_sub_chains". Proceeds in concert with
    that method as so:
        1: If the list of dominoes is empty, return the empty set.
        2: If there is only one domino provided and it has the same value on 
           each half, it is, technically, a solution, so return it.
        3: If there is more than one domino provided:
            1: Loop over each domino.
            2: Use build_sub_chains to build all possible chains with this
               domino as the first domino *without* rotating it.
            3: If there are any chains starting with this domino:
                1. Check whether the chain is a valid solution.
                2. If it is, immediately return it.
            4: If there are not, try rotating the domino and building chains
               starting with the rotated domino. If any check out, return them.
        4: At this point, either the provided dominoes are actually a single
           domino which does not form a valid chain, or every possible chain
           starting with every available domino and its rotation has been tried
           and found wanting.
        5: So return None.

    Parameters
    ----------
    dominoes : list[tuple]
        A list of dominoes (tuples) to attempt to form a chain of.

    Returns
    -------
    list[tuple]
        A list of dominoes forming a chain; the empty list if no dominoes were
        provided; or None if no chain could be formed.
    """
        
    if not dominoes:
        return []
            
    if len(dominoes) == 1:
       if dominoes[0][0] == dominoes[0][-1]:
           return dominoes
    else: 
        for domino in dominoes:
            rem_dominoes = copy.deepcopy(dominoes)
            rem_dominoes.remove(domino)
       
            candidates_normal = build_sub_chains(domino, rem_dominoes)
       
            if candidates_normal:
                for can in candidates_normal:
                    if valid_domino_chain(can):
                        return can
                
            rev_domino = domino[::-1]
       
            candidates_reversed = build_sub_chains(rev_domino, rem_dominoes)
       
            if candidates_reversed:
                for can in candidates_reversed:
                    if valid_domino_chain(can):
                        return can
               
    return None
