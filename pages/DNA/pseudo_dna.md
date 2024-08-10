# Pseudocode

**Function**: dna(dna_string)

- **Initialize** a dictionary called `counts` with keys 'A', 'C', 'G', 'T', each set to 0.
- **For each** character `nucleotide` in the input `dna_string`:
  - **If** `nucleotide` is a key in the `counts` dictionary:
    - **Increment** the value associated with that key by 1.
- **Return** the counts for 'A', 'C', 'G', and 'T' from the dictionary.


