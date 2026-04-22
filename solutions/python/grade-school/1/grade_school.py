""" Class for solving the Exercism Grade School exercise."""
class School:

    def __init__(self) -> None:
        """
        Constructor for the school roster.

        Returns
        -------
        None
        """
        
        self.students = {}
        self.inserted = [] # needed for some tests
        
    def _sort_dict(self) -> None:
        """
        Sorts the students dictionary by grade level and then student name.
        
        Encapsulating it as a separate method makes it easier to call it on
        output rather than after each input.

        Returns
        -------
        None
        """
        
        self.students = dict(sorted(self.students.items(), 
                                    key = lambda value: (value[-1], value[0])))

    def add_student(self, name: str, grade: int) -> None:
        """
        Adds a student to the roster and resorts it according to spec.

        Parameters
        ----------
        name : str
            Name of the student.
        grade : int
            Grade level of the student.

        Returns
        -------
        None
        """
        
        # Uses the fact that Python dictionaries throw a KeyError if you try to
        # use a key without having inserted it previously to detect when a name
        # is already present.
        try:
            self.students[name]
            self.inserted.append(False)
        except KeyError:
            self.students[name] = grade
            self.inserted.append(True)
            
    def roster(self) -> list[str]:
        """
        Returns the names of all enrolled students, sorted by grade level and
        then name.

        Returns
        -------
        list[str]
            The names of the enrolled students, regardless of grade.
        """
        
        self._sort_dict()
        
        return list(self.students.keys())

    def grade(self, grade_number: int) -> list[str]:
        """
        Returns the names of all enrolled students in the specified grade,
        sorted by name.

        Parameters
        ----------
        grade_number : int
            Grade level to provide student names for.

        Returns
        -------
        list[str]
            The names of the students enrolled in the specified grade.
        """
        
        self._sort_dict()
        
        return [student for student in self.students.keys() 
                if self.students[student] == grade_number]
        
    def added(self) -> list[bool]:
        """
        Returns a list of booleans indicating whether a student was added to
        the roster or not (due to another student with the same name already
        existing).

        Returns
        -------
        list[bool]
            See above.
        """
        return self.inserted
