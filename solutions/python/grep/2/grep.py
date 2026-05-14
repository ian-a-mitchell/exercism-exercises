""" 
Module for imitating grep...slowly and inefficiently. Solves grep exercise
on Exercism.
"""

import re

_NUM_LINES = "-n"
_IGNORE_CASE = "-i"
_WHOLE_LINE = "-x"
_INVERT_MATCH = "-v"
_LIST_FILE = "-l"

def grep_file(pattern: str, flags: list[str], file: str) -> list[str]:
    """
    Processes a single file according to the pattern and flags to return a list
    of strings that either match the pattern given the flags if _INVERT_MATCH
    is not set, or do not match the pattern given the flags if _INVERT_MATCH is
    set. If _NUM_LINES is set, each line is prepended with the line number and
    a colon.
    
    Parameters
    ----------
    pattern : str
        A word or phrase to match.
    flags : list[str]
        A list of strings to adjust certain behavior.
    file : str
        The name of the file to process.

    Returns
    -------
    list[str]
        A list containing all lines as described above.
    """
    
    with open(file, "r", encoding="ascii") as my_file:
        my_text = my_file.read().splitlines()
    
    r_pattern = fr"{pattern}"
    
    if _WHOLE_LINE in flags:
        r_pattern = "^" + r_pattern + "$"
    
    re_flags = 0
    
    output = []
    
    if _IGNORE_CASE in flags:
        re_flags = re_flags | re.IGNORECASE
        
    for idx, line in enumerate(my_text):
        patt_match = re.search(r_pattern, line, flags = re_flags)
        do_invert = _INVERT_MATCH in flags
        if bool(patt_match) ^ do_invert:
            new_line = line
            if _NUM_LINES in flags:
                new_line = f"{idx + 1}:" + new_line
            new_line += "\n"
            output.append(new_line)
    
    return output

def grep(pattern: str, flags: str, files: list[str]) -> str:
    """
    Processes a set of files according to the pattern and flags. The output is
    largely as above except that:
        1) the output is in the form of a multi-line string instead of a list;
        2) if more than one file is in the input, the name of the file is
           prepended to every line coming from that file;
        3) if _LIST_FILE is set, each file that has a match is listed instead
           of the full output.
    
    Parameters
    ----------
    pattern : str
        A word or phrase to match.
    flags : list[str]
        A list of strings to adjust certain behavior.
    files : list[str]
        The names of the files to process.

    Returns
    -------
    str
        A string containing each valid line from the files, separated by
        newlines, or a list of the files that contain matches if _LIST_FILE is
        set.
    """
    
    output = []
    
    split_flags = flags.split()
    
    for file in files:
        next_output = grep_file(pattern, split_flags, file)
        if next_output:
            if _LIST_FILE not in split_flags:
                prefix = ""
                if len(files) > 1:
                    prefix = file + ":"
                next_output = "".join([prefix + line for line in next_output])
                output.append(next_output)
            else:
                output.append(file + "\n")
        
    return "".join(output)
