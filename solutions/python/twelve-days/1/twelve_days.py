NUMS = {
   1: 'a',
   2: 'two',
   3: 'three',
   4: 'four',
   5: 'five',
   6: 'six',
   7: 'seven',
   8: 'eight',
   9: 'nine',
   10: 'ten',
   11: 'eleven',
   12: 'twelve'
}

CARDINALS = {
    1: 'first',
    2: 'second',
    3: 'third',
    4: 'fourth',
    5: 'fifth',
    6: 'sixth',
    7: 'seventh',
    8: 'eighth',
    9: 'ninth',
    10: 'tenth',
    11: 'eleventh',
    12: 'twelfth'
}

PHRASE = {
   1: 'Partridge in a Pear Tree',
   2: 'Turtle Doves',
   3: 'French Hens',
   4: 'Calling Birds',
   5: 'Gold Rings',
   6: 'Geese-a-Laying',
   7: 'Swans-a-Swimming',
   8: 'Maids-a-Milking',
   9: 'Ladies Dancing',
   10: 'Lords-a-Leaping',
   11: 'Pipers Piping',
   12: 'Drummers Drumming'
}

def verse_generator(verse_num):
    
    output = [f'On the {CARDINALS[verse_num]} day of Christmas my true love gave to me: ']
    
    for i in range(verse_num, 0, -1):
        if i > 1:
            output.append(f'{NUMS[i]} {PHRASE[i]}, ')
        else:
            if verse_num > 1:
                output.append('and ')
            output.append(f'{NUMS[i]} {PHRASE[i]}.')
    
    return ''.join(output)

def recite(start_verse, end_verse):
    
    output = [verse_generator(start_verse)]
    
    for i in range(start_verse + 1, end_verse + 1):
        output.append(verse_generator(i))
        
    return output
