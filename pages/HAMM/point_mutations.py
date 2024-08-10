def point_mutations(dna_string_a, dna_string_b):
    hamming_distance = 0

    if len(dna_string_a) != len(dna_string_b):
        return "DNA strings are not equal length"

    # loop through both strings at the same time
    for nucleotide in range(len(dna_string_a)):
        # compare the nucleotides at the same index
        if dna_string_a[nucleotide] != dna_string_b[nucleotide]:
            # if characters differ, increment hamming distance
            hamming_distance += 1

    return hamming_distance