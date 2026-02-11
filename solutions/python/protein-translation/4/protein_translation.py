from itertools import takewhile
import re

CODONS = r'[UAGC][UAGC][UAGC]'

STOP = 'STOP'

AMINOS = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': STOP,
    'UAG': STOP,
    'UGA': STOP
}

CODON_LEN = 3
        

def proteins(strand):
                
    output = list(takewhile(lambda x: x != STOP,
                    map(lambda x: AMINOS[x], re.findall(CODONS, strand))))
        
    return output
