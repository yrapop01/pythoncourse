import unittest
from divisors... import prime_divisors
 #https://github.com/yrapop01/pythoncourse
# python -m unittest

class TestStringMethods(unittest.TestCase):

    def test_1(self):
       prime_divisors(10) ==> [5, 2]

    def test_2(self):
       prime_divisors(1) ==> []

if __name__ == '__main__':
    unittest.main()
