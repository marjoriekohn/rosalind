# Pseudocode

**Function**: hamm(dna_string_a, dna_string_b)

- **Initialize** a variable `hamming_distance` to 0.
- **If** the length of `dna_string_a` is not equal to the length of `dna_string_b`:
  - **Return** "DNA strings are not equal length".
- **For each** index `nucleotide` from 0 to the length of `dna_string_a` (or `dna_string_b`):
  - **If** the nucleotide at position `nucleotide` in `dna_string_a` is not equal to the nucleotide at the same position in `dna_string_b`:
    - **Increment** `hamming_distance` by 1.
- **Return** the value of `hamming_distance`.
