import unittest
from reverse_complement import reverse_complement


class MyTestCase(unittest.TestCase):
    def test_reverse_complement(self):
        self.assertEqual(reverse_complement("GTCA"), "TGAC")

    def test_empty_string(self):
        self.assertEqual(reverse_complement(""), "Empty DNA string")

    def test_invalid_string(self):
        self.assertEqual(reverse_complement("ACXGT"), "Invalid nucleotide in string")


if __name__ == '__main__':
    unittest.main()
