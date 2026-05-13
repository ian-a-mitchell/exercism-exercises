"""
Module for solving the Scale Generator exercise on Exercism.
Given a specified starting note (tonic), determines the corresponding chromatic
scale, and further given a specified set of intervals can provide the diatonic
scale starting with the tonic for those intervals.
"""

class Scale:
    """
    Class which can provide chromatic and diatonic interval information given
    a starting note (tonic).
    """
    
    _SHARP = ("A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#")
    _FLAT = ("A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab")
    
    _SHARPS = {"C", "a", "G", "D", "A", "E", "B", "F#", "e", "b", "f#", "c#", 
               "g#", "d#"}
    
    _INTERVALS = {
        "A": 3,
        "M": 2,
        "m": 1
    }
                
    def __init__(self, tonic: str) -> None:
        """
        Given a tonic, builds a personal copy of the chromatic scale starting
        at that tonic. The tonic may
            1) start with a lower-case (minor scale) or upper case 
              (major scale) letter;
            2) May have a second character of:
                a: None
                b: Flat (b)
                c: Sharp (#)
        This affects whether the usual representation of the chromatic scale is
        the "sharp" or "flat" form. Therefore, the main work that the init
        function actually does is determine whether the sharp or flat form
        should be used before building the new list.
        
        Parameter:
            tonic : str
                A string representing the starting note or tonic, as described
                above.
        """
                    
        main_scale = Scale._SHARP if tonic in Scale._SHARPS else Scale._FLAT
        
        tonic_idx = main_scale.index(tonic[0].upper() + tonic[1:])
            
        self.chromat = list(main_scale[tonic_idx:] + main_scale[:tonic_idx])

    def chromatic(self) -> list[str]:
        """
        Returns this scale's version of the chromatic scale, i.e. the chromatic
        scale starting with the tonic provided to the constructor. Building
        the scale was done in the constructor.
        """
        
        return self.chromat

    def interval(self, intervals: str) -> list[str]:
        """
        Returns the series of notes starting with this scale's tonic and
        corresponding to the provided intervals. The interval codes are
        associated with step sizes above, in _INTERVALS. Allowable values are
            1: m, a "half step" (or step size of 1, i.e. to the next note)
            2: M, a "full step" (or step size of 2)
            3: A, an "augmented second" (or step size of 3)
        
        Parameter:
            intervals : str
                A string representing a series of intervals corresponding to a
                diatonic scale.
        
        Output:
            list[str]
                A list of strings stating the notes of the given diatonic scale
                given the chromatic scale encoded by this instance.
        """
                
        step_size = [Scale._INTERVALS[char] for char in intervals]
                
        stops = [sum(step_size[:idx]) % len(self.chromat) 
                 for idx in range(len(step_size) + 1)]
                            
        return [self.chromat[stop] for stop in stops]
