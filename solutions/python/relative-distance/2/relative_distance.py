""" A module solving the Relative Distances problem on Exercism. """

import copy
import heapq

class RelativeDistance:
    """
    A class that stores a family tree tracking the degree-one relatives
    (parent, child, or sibling) of each person in the tree, and provides a
    method for calculating the degree of consangunity between any two people
    represented in the tree.
    """
    def __init__(self, family_tree: dict):
        """
        Sets up the family tree. This is slightly different from the input in
        two main respects. First, it uses sets rather than lists to store the
        names of degree-one relatives. Second, it associates with each person
        the set of degree-one relatives they have rather than just their
        children (if any); that is, the value associated with each person is
        the set of their parent(s), siblings, and children.
        
        Additionally, a flat set containing all of the names is also created.
        This is useful for checking whether someone is in the family tree at
        all.

        Parameters
        ----------
        family_tree : dict
            A dictionary consisting of a string representing a person's name
            and a list of strings corresponding to that person's children, if
            any.

        Returns
        -------
        None
        """
        self._names = set()
        
        for parent, children in family_tree.items():
            self._names.add(parent)
            for child in children:
                self._names.add(child)
                
        # Converts the original dictionary of strings and lists to one using
        # sets for representing the degree-one relatives.
        # It also promotes everyone to the key level, rather than hiding
        # children without their own children in the values.
        parent_tree = {}
        for name in self._names:
            try:
                children = family_tree[name]
            except KeyError:
                parent_tree[name] = set()
            else:
                parent_tree[name] = set(children)
                
        self._family_tree = copy.deepcopy(parent_tree)
        
        # Adds sibling-sibling and child-parent relationship to the vertices.
        # Note the use of a copy storing only parent-child relationships to
        # avoid issues from updating the parent's relationships using their
        # child's relationships.
        for parent, children in parent_tree.items():
            for child in children:
                child_children = parent_tree[child]
                siblings = copy.deepcopy(children)
                siblings.remove(child) #eliminates loops
                
                degree_one_child = child_children | siblings
                degree_one_child.add(parent)
                
                self._family_tree[child] = degree_one_child

    def degree_of_separation(self, person_a: str, person_b: str) -> int:
        """
        Calculates the distance between Person A and Person B on the graph
        using Dijkstra's algorithm with all weights set equal to one (in other
        words, all of the noted connections are degree-one relationships). This
        could also be phrased as calculating the degree of consangunity between
        Person A and Person B.
    
        Also does error handling in the cases where:
            1: Person A is not in the family tree;
            2: Person B is not in the family tree;
            3: There is no specified link between Person A and Person B.

        Parameters
        ----------
        person_a : str
            The name of one of the people to calculate the distance between.
        person_b : str
            The name of the other person to calculate the distance between.

        Returns
        -------
        int
            The degree of consangunity or distance between Person A and Person
            B on the graph. The minimum value is zero (Person A and Person B
            are the same), and the maximum is essentially something like the
            number of people who have ever lived (in practice smaller due to
            various social and historical factors).

        Raises
        ------
        ValueError
            Per specification, ValueError is raised in each of the three
            conditions named above.
        """
        
        if person_a not in self._names:
            raise ValueError("Person A not in family tree.")
        if person_b not in self._names:
            raise ValueError("Person B not in family tree.")
            
        # Dijkstra's algorithm with all weights = 1
        distances = {name: len(self._names) + 1 for name in self._family_tree}
        distances[person_a] = 0
        
        priority = [(0, person_a)]
        heapq.heapify(priority)
        
        visited = set()
                
        while priority:
            current_distance, current_person = heapq.heappop(priority)
            
            if current_person in visited:
                continue # avoids backtracking
            visited.add(current_person)
            
            for relative in self._family_tree[current_person]:
                tentative_distance = current_distance + 1
                if tentative_distance < distances[relative]:
                    distances[relative] = tentative_distance
                    heapq.heappush(priority, (tentative_distance, relative))
                                    
        if distances[person_b] > len(self._names):
            raise ValueError("No connection between person A and person B.")
                    
        return distances[person_b]
        
