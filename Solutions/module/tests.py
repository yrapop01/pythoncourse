import unittest
from divisors... import prime_divisors

# python -m unittest

class TestStringMethods(unittest.TestCase):

    def test_1(self):
       prime_divisors(10) ==> [5, 2]

    def test_2(self):
       prime_divisors(1) ==> []

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertFalse('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
