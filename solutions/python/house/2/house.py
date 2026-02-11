START = "This is"
NOUN_VERB = {
    1: ("house that Jack built",),
    2: ("malt", "lay in"),
    3: ("rat", "ate"),
    4: ("cat", "killed"),
    5: ("dog", "worried"),
    6: ("cow with the crumpled horn", "tossed"),
    7: ("maiden all forlorn", "milked"),
    8: ("man all tattered and torn", "kissed"),
    9: ("priest all shaven and shorn", "married"),
    10: ("rooster that crowed in the morn", "woke"),
    11: ("farmer sowing his corn", "kept"),
    12: ("horse and the hound and the horn", "belonged to")
}

def build_verse(n):
    
    output = [f"{START} "]
    
    core = list(map(lambda x: f"the {NOUN_VERB[x][0]} that {NOUN_VERB[x][1]} ",
                    range(n, 1, -1)))
    
    output.extend(core)
    
    output.append(f"the {NOUN_VERB[1][0]}.")
    
    return ''.join(output)

def recite(start_verse, end_verse):
        
    output = list(map(build_verse, range(start_verse, end_verse + 1)))
            
    return output