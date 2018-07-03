import unittest
from divisors.prime import prime_divisors as divisors

class TestDivisors(unittest.TestCase):
    def test_ten(self):
        self.assertEqual(set(divisors(10)), {5, 2})

    def test_one(self):
        self.assertFalse(bool(list(divisors(1))))

if __name__ == '__main__':
    unittest.main()
