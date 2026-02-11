from itertools import takewhile
from textwrap import wrap

# Covers all standard amino acids because why not?
PHE = 'Phenylalanine'
LEU = 'Leucine'
ILE = 'Isoleucine'
MET = 'Methionine'
VAL = 'Valine'
SER = 'Serine'
PRO = 'Proline'
THR = 'Threonine'
ALA = 'Alanine'
TYR = 'Tyrosine'
HIS = 'Histidine'
GLN = 'Glutamine'
ASN = 'Asparagine'
LYS = 'Lysine'
ASP = 'Aspartic acid'
GLU = 'Glutamic acid'
CYS = 'Cysteine'
TRP = 'Tryptophan'
ARG = 'Arginine'
GLY = 'Glycine'

STOP = 'STOP'

AMINOS = {
    'UUU': PHE,
    'UUC': PHE,
    'UUA': LEU,
    'UUG': LEU,
    'CUU': LEU,
    'CUC': LEU,
    'CUA': LEU,
    'CUG': LEU,
    'AUU': ILE,
    'AUC': ILE,
    'AUA': ILE,
    'AUG': MET,
    'GUU': VAL,
    'GUC': VAL,
    'GUA': VAL,
    'GUG': VAL,
    'UCU': SER,
    'UCC': SER,
    'UCA': SER,
    'UCG': SER,
    'CCU': PRO,
    'CCC': PRO,
    'CCA': PRO,
    'CCG': PRO,
    'ACU': THR,
    'ACC': THR,
    'ACA': THR,
    'ACG': THR,
    'GCU': ALA,
    'GCC': ALA,
    'GCA': ALA,
    'GCG': ALA,
    'UAU': TYR,
    'UAC': TYR,
    'CAU': HIS,
    'CAC': HIS,
    'CAA': GLN,
    'CAG': GLN,
    'AAU': ASN,
    'AAC': ASN,
    'AAA': LYS,
    'AAG': LYS,
    'GAU': ASP,
    'GAC': ASP,
    'GAA': GLU,
    'GAG': GLU,
    'UGU': CYS,
    'UGC': CYS,
    'UGG': TRP,
    'CGU': ARG,
    'CGC': ARG,
    'CGA': ARG,
    'CGG': ARG,
    'AGU': SER,
    'AGC': SER,
    'AGA': ARG,
    'AGG': ARG,
    'GGU': GLY,
    'GGC': GLY,
    'GGA': GLY,
    'GGG': GLY,
    'UAA': STOP,
    'UAG': STOP,
    'UGA': STOP
}

CODON_LEN = 3

def translate(codon):
    
    output = ''
    
    try:
        output = AMINOS[codon]
    except:
        raise ValueError('invalid codon')
        
    return output

def proteins(strand):
                
    output = list(takewhile(lambda x: x != STOP,
                  map(translate, wrap(strand, CODON_LEN))))
        
    return output
