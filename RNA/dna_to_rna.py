# Instructions:
# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
# Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.
# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

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
