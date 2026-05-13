""" 
Module that processes a subset of Markdown tags into HTML tags. Solution to
the Exercism Markdown exercise.
"""

import re

_EMPHASIS_TAGS = {
    r"__([^\n]+?)__": ("<strong>", "</strong>"),
    r"_([^\n]+?)_": ("<em>", "</em>")
}

def parse(markdown: str) -> str:
    """
    Given a string formatted with a subset of Markdown syntax, converts
    those Markdown tags into HTML tags. This version tries to do as much as
    possible directly in regular expressions. Partial credit to lynx771 for
    this solution (I made some modifications)

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
    for pattern in _EMPHASIS_TAGS:
        tags = _EMPHASIS_TAGS[pattern]
        repl = tags[0] + r'\1' + tags[1]
        
        markdown = re.sub(pattern, repl, markdown)
    
    markdown = re.sub(r"^\* (.*?$)", r"<li>\1</li>", markdown, flags = re.M)
    markdown = re.sub(r"(<li>.*</li>)", r"<ul>\1</ul>", markdown, flags = re.S)
    
    header_pattern = r"(^#+) (.*?$)"
    if re.match(header_pattern, markdown, flags = re.M):
        hashes = len(re.match(header_pattern, markdown, flags = re.M).group(1))
        if hashes < 7:
            repl = fr"<h{hashes}>\2</h{hashes}>"
            markdown = re.sub(header_pattern, repl, markdown, flags = re.M)
            
    markdown = re.sub(r"^(?!<[hlu])(.*?$)", r"<p>\1</p>", markdown, flags=re.M)
    markdown = re.sub(r"\n", "", markdown)
        
    return markdown
