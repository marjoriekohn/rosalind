def hamm(dna_string_a, dna_string_b):
    hamming_distance = 0

    if len(dna_string_a) != len(dna_string_b):
        return "DNA strings are not equal length"

    for nucleotide in range(len(dna_string_a)):
        if dna_string_a[nucleotide] != dna_string_b[nucleotide]:
            hamming_distance += 1

    return hamming_distance
