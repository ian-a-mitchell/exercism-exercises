import re

_EMPHASIS_TAGS = {
    r"__(.*)__": ("<strong>", "</strong>"),
    r"_(.*)_": ("<em>", "</em>")
}

_PARA_TAGS = (r"<p>", r"</p>")

def _header_convert(line: str) -> str:
    """
    Given a line of text formatted in Markdown, converts header tags in the
    form of 1 to 6 "#" symbols at the beginning of the line into the equivalent
    HTML tag "<hn>," n being equivalent to the number of "#" symbols. Also
    adds a closing tag "</hn>" to the end of the line.
    
    If no header tags are present, no change is made.

    Parameters
    ----------
    line : str
        A line of string which may have Markdown header tags.

    Returns
    -------
    str
        The input line modified as described above.
    """
    
    output = line
    
    header_pattern = r"#+ "
    
    if re.match(header_pattern, line):
        hashes = len(re.match(header_pattern, line).group()) - 1
        if hashes < 7: # no h7+ level and tests show hashes should be kept
            core = f"h{hashes}>"
            output = f"<{core}{line[hashes + 1:]}</{core}"
    
    return output

def _emphasis_convert(line: str, pattern: str) -> str:
    """
    Given a line of text formatted in Markdown, converts a chosen emphasis tag
    into its HTML equivalent. The options are "__" or bolding, which converts
    into "<strong>" and "</strong>" tags and "_" or italicization, which
    converts into "<em>" and "</em>" tags.
    
    Basically finds and replaces paired instances of these tags until there are
    none left.
    
    Note that re.search returns the _first_ location that matches the pattern.

    Parameters
    ----------
    line : str
        A line of Markdown-formatted text which may or may not have emphasis
        tags as described above.
    pattern : str
        A pattern to use when looking for emphasis tags. Essentially eliminates
        duplication of code between bold and italic tag processing.

    Returns
    -------
    str
        The input line modified as described above.
    """
    
    tags = _EMPHASIS_TAGS[pattern]
    
    output = line
    
    while len(re.findall(pattern, output)) > 0:
        em_match = re.search(pattern, output)
        repl = f"{tags[0]}{em_match.group(1)}{tags[1]}"
        
        output = re.sub(pattern, repl, output, count = 1)
        
    return output

def _list_convert(line: str, in_list: bool) -> tuple[str, bool]:
    """
    Given a line of code formatted in Markdown, identifies any list tags that 
    might be present in the form of "* " into the equivalent HTML tags for the
    line, "<li>" at the beginning and "</li>" at the end.
    
    Additionally, using the "in_list" parameter, it identifies if a list has 
    started, which requires adding a "<ul>" tag in front, or if a list has 
    ended, which requires adding a "</ul>" tag...also to the front of the list.
    This is because it is easier to check whether a line is not a list even
    though the previous line was a list than checking whether the next line
    is a list.
    
    Parameters
    ----------
    line : str
        The line of text to add list tags to if applicable.
    in_list : bool
        True if the previous line was a list, False otherwise.

    Returns
    -------
    str
        The line modified as described above.
    bool
        True if this line was a list, False otherwise.
    """
    
    list_pattern = r"\* "
    list_trip = re.match(list_pattern, line)
    
    still_list = False
    output = line
    
    if list_trip:
        still_list = True
        output = f"<li>{line[2:]}</li>"
        if not in_list:
            output = "<ul>" + output
    elif in_list:
        output = r"</ul>" + output
            
    return (output, still_list)

def _para_convert(line: str) -> str:
    """
    Adds paragraph open and close tags to every line that isn't a header or
    list, and doesn't already have paragraph start tags.

    Parameters
    ----------
    line : str
        Line of text to potentially add paragraph tags to.

    Returns
    -------
    str
        Input text modified with paragraph tags if needed.
    """
    
    open_pattern = r"<h[1-6]>|<ul>|<p>|<li>"
    close_pattern = r"</\w+>"
    
    output = line
    
    if not re.match(open_pattern, line):
        # If we're here, we always want to add the close tags to the end.
        output += _PARA_TAGS[1]
        
        # If </ul> was added above, <p> needs to be added *after* it.
        if re.match(close_pattern, line):
            close_idx = output.index(">") + 1
            output = output[:close_idx] + _PARA_TAGS[0] + output[close_idx:]
        else:
            output = _PARA_TAGS[0] + output
            
    return output

def _parse_line(line: str, in_list: bool) -> tuple[str, bool]:
    """
    Given a line of text, applies all Markdown formatting rules to it and
    returns it along with an indication of whether this line was a list.

    Parameters
    ----------
    line : str
        String containing a line of text to reformat as Markdown.
        
    in_list: bool
        Boolean indicating whether the previous line was a list.

    Returns
    -------
    str
        Input text modified by applying the Markdown formatting rules to it.
    bool
        Boolean indicating whether this line was part of a list.
    """
    
    output = line
    
    for pattern in _EMPHASIS_TAGS:
        output = _emphasis_convert(output, pattern)
        
    output = _header_convert(output)
    output, still_list = _list_convert(output, in_list)
    output = _para_convert(output)
    
    return (output, still_list)

def parse(markdown: str) -> str:
    """
    Given a string formatted with a subset of Markdown syntax, converts
    those Markdown tags into HTML tags.

    Parameters
    ----------
    markdown : str
        String containing an arbitrary number of lines of text to reformat as 
        Markdown.

    Returns
    -------
    str
        Input text with Markdown tags substituted with HTML tags.
    """
    lines = markdown.splitlines()
    output = []
    in_list = False
    
    for line in lines:
        new_line, in_list = _parse_line(line, in_list)
        output.append(new_line)
        
    # if the last line is still a list, closes it
    if in_list:
        output.append("</ul>")
    return "".join(output)
