POLYMERASE = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}

def to_rna(dna_strand):
    
    return ''.join(list(map(lambda x: POLYMERASE[x], tuple(dna_strand))))
