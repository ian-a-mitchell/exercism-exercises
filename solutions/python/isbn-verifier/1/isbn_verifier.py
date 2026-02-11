import re

ISBN_LENGTH = 10

# Check whether the stripped ISBN-10 has ten characters
def length_check(isbn):
    
    return len(isbn) == ISBN_LENGTH

# Check whether the ISBN-10 has only the characters 0-9 and X
# Also check whether the first 9 characters are only 0-9 (X is not allowed)
def content_check(isbn):
    
    f = re.compile(r'[^\dX]+')
        
    fnf = re.compile(r'\D+')
    
    return f.match(isbn[-1]) is None and fnf.search(isbn[0:9]) is None

# Calculate the checksum of the ISBN and verify it against the check digit
def checksum(isbn):
    
    isbn = [10 if x == 'X' else int(x) for x in isbn]
    
    check_table = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    # Checksum is dot product of ISBN w/check table    
    return sum([i * j for i, j in zip(isbn, check_table)]) % 11 == 0

def is_valid(isbn):
    
    isbn = re.sub('-', '', isbn.upper())
    
    return length_check(isbn) and content_check(isbn) and checksum(isbn)
