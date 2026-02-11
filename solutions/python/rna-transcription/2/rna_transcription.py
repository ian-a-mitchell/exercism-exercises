POLYMERASE = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}

def to_rna(dna_strand):
    
    return str.translate(dna_strand, str.maketrans(POLYMERASE))
