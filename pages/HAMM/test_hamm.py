import unittest
from hamm import point_mutations


class MyTestCase(unittest.TestCase):
    def test_0_hamming_distance(self):
        self.assertEqual(point_mutations("ACGT", "ACGT"), 0)  # no difference

    def test_1_hamming_distance(self):
        self.assertEqual(point_mutations("ACGT", "TCGT"), 1)  # one difference

    def test_different_lengths(self):
        self.assertEqual(point_mutations("ACGTACGT", "ACGT"), "DNA strings are not equal length")  # dna strings of different length


if __name__ == '__main__':
    unittest.main(verbosity=2)
