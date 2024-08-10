import unittest
from fib import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_sample_data(self):
        self.assertEqual(fibonacci(5, 3), 19)  # sample dataset and output


if __name__ == '__main__':
    unittest.main()
