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
