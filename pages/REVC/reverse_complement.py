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
