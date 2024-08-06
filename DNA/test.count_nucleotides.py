import unittest
from DNA.count_nucleotides import count_nucleotides


class TestCountNucleotides(unittest.TestCase):
    def test_all_nucleotides(self):
        self.assertEqual(count_nucleotides("ACGTACGT"), (2, 2, 2, 2))  # all nucleotides present

    def test_a_nucleotides(self):
        self.assertEqual(count_nucleotides("AAAA"), (4, 0, 0, 0))  # only 'A' nucleotides present

    def test_c_nucleotides(self):
        self.assertEqual(count_nucleotides("CCCC"), (0, 4, 0, 0))  # only 'C' nucleotides present

    def test_g_nucleotides(self):
        self.assertEqual(count_nucleotides("GGGG"), (0, 0, 4, 0))  # only 'G' nucleotides present

    def test_t_nucleotides(self):
        self.assertEqual(count_nucleotides("TTTT"), (0, 0, 0, 4))  # only 'T' nucleotides present

    def test_empty_nucleotides(self):
        self.assertEqual(count_nucleotides(""), (0, 0, 0, 0))  # empty string

    def test_invalid_nucleotides(self):
        self.assertEqual(count_nucleotides("ACGTXACGT"), (2, 2, 2, 2))  # invalid characters


if __name__ == '__main__':  # This block ensures the following code is run only if this script is executed directly
    unittest.main(verbosity=2)  # Run the test cases
