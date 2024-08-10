def dna_to_rna(dna_string):
    rna_string = []

    if dna_string == '':
        return 'Empty DNA string'

    for nucleotide in dna_string:
        if nucleotide == 'T':
            rna_string.append('U')
        elif nucleotide in 'AGC':
            rna_string.append(nucleotide)
        else:
            return "Invalid nucleotide in string"
    return ''.join(rna_string)
