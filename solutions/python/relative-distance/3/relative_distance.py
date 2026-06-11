""" A module solving the Relative Distances problem on Exercism. """

import heapq

class RelativeDistance:
    """
    A class that stores a family tree tracking the degree-one relatives
    (parent, child, or sibling) of each person in the tree, and provides a
    method for calculating the degree of consangunity between any two people
    represented in the tree.
    """
    def __init__(self, family_tree: dict[str, list[str]]):
        """
        Sets up the family tree. This is slightly different from the input in
        two main respects. First, it uses sets rather than lists to store the
        names of degree-one relatives. Second, it associates with each person
        the set of degree-one relatives they have rather than just their
        children (if any); that is, the value associated with each person is
        the set of their parent(s), siblings, and children.
        
        Also creates a flat set of names (keys) for use at various points.

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
                
        self._family_tree: dict[str, set[str]] = {}
        for parent, children in family_tree.items():
            if parent not in self._family_tree:
                self._family_tree[parent] = set(children)
            else:
                exist_children = self._family_tree[parent]
                self._family_tree[parent] = set(children) | exist_children
            
            # Sets up children as full members of the tree and ensures the
            # sets represent degree-one relatives and not just children.
            for idx, child in enumerate(children):
                if child not in self._family_tree:
                    self._family_tree[child] = set()
                degree_one = set([parent]) | set(children[:idx])
                degree_one = degree_one | set(children[idx + 1:])
                self._family_tree[child] = degree_one
                
        self._names = set(self._family_tree.keys())

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
        distances = {name: len(self._names) + 1 for name in self._names}
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
        
