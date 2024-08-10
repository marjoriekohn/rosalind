# Pseudocode

**Function**: revc(dna_string)

- **Initialize** an empty list called `reverse_complement_dna`.
- **Define** a dictionary called `complement` with mappings:
  - 'A' to 'T'
  - 'C' to 'G'
  - 'G' to 'C'
  - 'T' to 'A'

- **If** `dna_string` is empty:
  - **Return** "Empty DNA string".

- **For each** nucleotide in `dna_string`:
  - **If** the nucleotide is in the `complement` dictionary:
    - **Append** the corresponding complement nucleotide to `reverse_complement_dna`.
  - **Else**:
    - **Return** "Invalid nucleotide in string".

- **Return** the string formed by joining the elements of `reverse_complement_dna` in reverse order.
