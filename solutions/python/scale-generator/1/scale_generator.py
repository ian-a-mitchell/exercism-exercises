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
    
    _SHARP_CHR = ("A", "A#", "B", "C", "C#", "D", 
                 "D#", "E", "F", "F#", "G", "G#")
    _FLAT_CHR = ("A", "Bb", "B", "C", "Db", "D",
                 "Eb", "E", "F", "Gb", "G", "Ab")
    
    _MAJ_SHARP = {"C", "G", "D", "A", "E", "B", "F#"}
    _MAJ_FLAT = {"F", "Bb", "Eb", "Ab", "Db", "Gb"}
    _MIN_SHARP = {"A", "E", "B", "F#", "C#", "G#", "D#"}
    _MIN_FLAT = {"D", "G", "C", "F", "Bb", "Eb"}
    
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
        
        is_minor = tonic[0].islower()
        tonic = tonic.upper() if len(tonic) == 1 else tonic[0].upper() + tonic[1:]
            
        is_sharp = tonic in Scale._MIN_SHARP if is_minor else tonic in Scale._MAJ_SHARP
        
        main_scale = Scale._SHARP_CHR if is_sharp else Scale._FLAT_CHR
        start_idx = main_scale.index(tonic)
            
        self.chromat = [main_scale[idx % len(main_scale)] 
                    for idx in range(start_idx, start_idx + len(main_scale))]

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
        
        output = [self.chromat[0]]
        idx = 0
        
        for char in intervals:
            idx += Scale._INTERVALS[char]
            idx %= len(self.chromat)
            
            output.append(self.chromat[idx])
            
        return output
