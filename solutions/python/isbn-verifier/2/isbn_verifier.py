import re

ISBN_LENGTH = 10

# Check whether the stripped ISBN-10 has ten characters
def length_check(isbn):
    
    return len(isbn) == ISBN_LENGTH

# Check whether the ISBN-10 has only the characters 0-9 and X
# X is coerced to '10' in preprocessing
def content_check(isbn):
            
    f = re.compile(r'\D+')
    
    return f.match(str(isbn)) is None

# Calculate the checksum of the ISBN and verify it against the check digit
def checksum(isbn):
    
    isbn = [int(x) for x in isbn]
    
    # Checksum is dot product of ISBN w/check table    
    return sum([i * j for i, j in zip(isbn, range(10, 0, -1))]) % 11 == 0

def is_valid(isbn):
    
    isbn = list(re.sub('-', '', isbn.upper()))
    
    if(isbn[-1] == 'X'):
        isbn[-1] = '10'
    
    return length_check(isbn) and content_check(isbn) and checksum(isbn)
