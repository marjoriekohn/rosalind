# Instructions
# Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s.
# As a result, t must be no longer than s.
# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

def motif_dna(dna_string, dna_substring):
    substring_locations = []

    # edge case: dna_substring must be no longer than dna_string
    if len(dna_substring) > len(dna_string) or len(dna_substring) == 0:
        return "ERROR: dna_substring is longer than dna_string"

    # loop through dna_string, within valid starting positions
    for index in range(len(dna_string) - len(dna_substring) + 1):
        # slicing, check if sliced string matches substring
        if dna_string[index: index + len(dna_substring)] == dna_substring:
            # if it does, add it to the array of locations
            substring_locations.append(index + 1)

    return ' '.join(map(str, substring_locations))
