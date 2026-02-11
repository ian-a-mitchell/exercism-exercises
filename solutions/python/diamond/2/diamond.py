from string import ascii_uppercase

def gen_row(i, n):
    
    row = list(range(n)) + list(range(n, -1, -1))
    row_letter = ascii_uppercase[i]
    
    row = ''.join(list(map(lambda x: row_letter if x == n - i else ' ', row)))
        
    return row

def rows(letter):
    
    n = ascii_uppercase.index(letter.upper())
            
    rows = list(range(n)) + list(range(n, -1, -1))
    
    output = list(map(lambda x: gen_row(x, n), rows))
    
    return output