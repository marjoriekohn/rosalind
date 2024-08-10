import unittest
from pages.DNA.dna import dna


class TestCountNucleotides(unittest.TestCase):
    def test_all_nucleotides(self):
        self.assertEqual(dna("ACGTACGT"), (2, 2, 2, 2))  # all nucleotides present

    def test_a_nucleotides(self):
        self.assertEqual(dna("AAAA"), (4, 0, 0, 0))  # only 'A' nucleotides present

    def test_c_nucleotides(self):
        self.assertEqual(dna("CCCC"), (0, 4, 0, 0))  # only 'C' nucleotides present

    def test_g_nucleotides(self):
        self.assertEqual(dna("GGGG"), (0, 0, 4, 0))  # only 'G' nucleotides present

    def test_t_nucleotides(self):
        self.assertEqual(dna("TTTT"), (0, 0, 0, 4))  # only 'T' nucleotides present

    def test_empty_nucleotides(self):
        self.assertEqual(dna(""), (0, 0, 0, 0))  # empty string

    def test_invalid_nucleotides(self):
        self.assertEqual(dna("ACGTXACGT"), (2, 2, 2, 2))  # invalid characters


if __name__ == '__main__':  # This block ensures the following code is run only if this script is executed directly
    unittest.main(verbosity=2)  # Run the test cases
