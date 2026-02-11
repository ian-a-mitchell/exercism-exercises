from itertools import takewhile
from textwrap import wrap

CODONS = {
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
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP'
}

CODON_LEN = 3

def not_stop(protein):
    
    return protein != 'STOP'

def proteins(strand):
                
    output = list(takewhile(not_stop,
                  list(map(lambda x: CODONS[x], wrap(strand, CODON_LEN)))))
    
    return output
