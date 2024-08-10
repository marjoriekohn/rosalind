import unittest
from dna_to_rna import dna_to_rna


class MyTestCase(unittest.TestCase):

    def test_valid_nucleotides(self):
        self.assertEqual(dna_to_rna("ACGT"), "ACGU")  # valid nucleotides present

    def test_invalid_nucleotides(self):
        self.assertEqual(dna_to_rna("TXACG"), "Invalid nucleotide in string")  # invalid nucleotide present

    def test_empty_nucleotides(self):
        self.assertEqual(dna_to_rna(""), "Empty DNA string")  # empty string as input


if __name__ == '__main__':
    unittest.main(verbosity=2)
