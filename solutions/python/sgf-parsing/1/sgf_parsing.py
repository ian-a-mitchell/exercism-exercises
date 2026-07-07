import re

class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other
    
    def __hash__(self):
        
        return hash(self.properties.items()) + hash(tuple(self.children))
    
def validate_string(input_string: str) -> None:
    
    no_tree = False
    
    if not input_string:
        no_tree = True
    # This has the problem that it doesn't check that *all* trees are properly
    # done, just the first one.
    # but this is called again later...
    elif not re.match(r"\(.*\)", input_string, re.DOTALL):
        no_tree = True
                
    if no_tree:
        raise ValueError("tree missing")
        
    # This also only checks the first tree that appears
    if not re.match(r"\(;.*\)", input_string, re.DOTALL):
        raise ValueError("tree with no nodes")

def validate_key(candidate_key: str) -> None:
    
    if not re.match(r"[A-Z]", candidate_key) or re.match(r"[A-Z]", candidate_key).group() != candidate_key:
        raise ValueError("property must be in uppercase")
        
def validate_head(head_string: str) -> bool:
    
    head = re.match(r"\(;.*;[A-Z]", head_string, re.DOTALL)
    if not head:
        head = re.match(r"\(;.*\(", head_string, re.DOTALL)
        
    if head:
        return True
    
    return False

def get_head(input_string: str) -> str:
    
    head = []
    
    head_end = 1
    
    while head_end < len(input_string) and not validate_head("".join(head)):
        head_end += 1
        head = input_string[0:head_end]
        
    head = "".join(head)
    
    if head[-1] == "(":
        head = head[1:-1]
    else:
        head = head[1:-2]
        
    return head
    
def parse(input_string):
    
    validate_string(input_string)
    
    head = get_head(input_string)
        
    tail = input_string.replace(head, "")
    
    properties = {}
    key_match = re.compile(r"[;\]]+[A-Za-z]+\[", re.DOTALL)
    
    keys = key_match.findall(head)
    for idx, key in enumerate(keys):
        validate_key(key[1:-1])
        keys[idx] = key[1:-1]
        
    if not keys:
        raise ValueError("properties without delimiter")
        
    values = key_match.split(head)
    
    if not values[0]:
        values.pop(0)
        
    for key, value in zip(keys, values):
        multi_value = re.compile(r"\]\[", re.DOTALL)
        split_value = multi_value.split(value)
        
        for idx, value in enumerate(split_value):
            if value[-1] == "]":
                split_value[idx] = value[:-1]
                
        properties[key] = split_value
        
    seeds = re.findall(r"\(;.*\)", tail, re.DOTALL)
    
    children = []
    
    for seed in seeds:
        split_seed = re.split(r"\)\(", seed, re.DOTALL)
        
        for idx, value in enumerate(split_seed):
            if value[0] != "(":
                value = "(" + value
            if value[-1] != ")":
                value = value + ")"
            if value[-2:] == "))":
                value = value[:-1]
                
            split_seed[idx] = value
                
        for child in split_seed:
            children.append(parse(child))
            
    output = SgfTree(properties, children)
        
    return output
