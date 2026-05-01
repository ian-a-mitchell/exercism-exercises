""" Module for solving the Kindergarten Garden problem on Exercism. """

class Garden:
    """ 
    Class storing data on the plants associated with the students of a
    kindergarten class.
    """
    
    _PLANT_TRANSLATE = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets"
    }
    
    # Since none of the non-track-specific problems bother explicitly telling
    # you who is in the class...
    _DEFAULT_STUDENTS = (
        "Alice", 
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Fred",
        "Ginny",
        "Harriet",
        "Ileana",
        "Joseph",
        "Kincaid",
        "Larry"
    )
    
    def __init__(self, diagram: list[str], students: list[str]=list(_DEFAULT_STUDENTS)):
        """
        Creates the garden object. Where all of the actual work takes place.
        
        The main effort is in stepping through the diagram to join together
        the correct plants from both rows.

        Parameters
        ----------
        diagram : list[str]
            A list of strings showing the plants on both rows of a kindergarten
            garden according to the codes in _PLANT_TRANSLATE.
        students : list_str, optional
            A list of student names. The default is _DEFAULT_STUDENTS.

        Returns
        -------
        None
        """
        
        split_diagram = diagram.splitlines()
        # This handles the case where no explicit student list is provided
        # but only some students can have plants.
        students = sorted(students)[:len(split_diagram[0]) // 2:]
        
        self.labeled_garden = {}
        
        for idx, student in enumerate(students):
            plants = [row[idx * 2: idx * 2 + 2] for row in split_diagram]
            plants = list("".join(plants))
            plants = [Garden._PLANT_TRANSLATE[plant] for plant in plants]
            self.labeled_garden[student] = plants
    
    def plants(self, student: str):
        """ Returns the plants for the student named student. """
        
        return self.labeled_garden[student]