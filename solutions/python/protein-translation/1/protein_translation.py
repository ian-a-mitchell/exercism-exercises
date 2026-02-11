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

def proteins(strand):
        
    output = []
    
    for i in range(0, len(strand), CODON_LEN):
        protein = CODONS[strand[i:i + CODON_LEN:1]]
        
        if protein == 'STOP':
            break
        else:
            output.append(protein)
    
    return output
