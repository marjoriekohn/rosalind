# Instructions:
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

def reverse_complement(dna_string):
    reverse_complement_dna = []
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

    if dna_string == "":
        return "Empty DNA string"

    for nucleotide in dna_string:
        if nucleotide in complement:
            reverse_complement_dna.append(complement[nucleotide])
        else:
            return "Invalid nucleotide in string"

    return ''.join(reversed(reverse_complement_dna))
