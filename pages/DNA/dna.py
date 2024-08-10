def dna(dna_string):
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for nucleotide in dna_string:
        if nucleotide in counts:
            counts[nucleotide] += 1

    return counts['A'], counts['C'], counts['G'], counts['T']
