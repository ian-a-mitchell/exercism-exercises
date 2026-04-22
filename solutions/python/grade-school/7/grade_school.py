""" Class for solving the Exercism Grade School exercise."""
class School:
    """ Class for solving the Exercism Grade School exercise."""

    def __init__(self) -> None:
        """
        Constructor for the school roster.

        Returns
        -------
        None
        """
        
        self._students = {} # student_name : grade
        self._inserted = [] # needed for some tests
        
    def _sort_dict(self) -> None:
        """
        Sorts the _students dictionary by grade level and then student name.
        
        Encapsulating it as a separate method makes it easier to call it on
        output rather than after each input.

        Returns
        -------
        None
        """
        
        self._students = dict(sorted(self._students.items(), 
                                    key = lambda value: (value[-1], value[0])))

    def add_student(self, name: str, grade: int) -> None:
        """
        Adds a student to the roster.

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
        
        if name in self._students:
            self._inserted.append(False)
        else:
            self._students[name] = grade
            self._inserted.append(True)
            
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
        
        return list(self._students.keys())

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
        
        return [student_name for student_name, student_grade 
                in self._students.items() if student_grade == grade_number]
        
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
        return self._inserted
