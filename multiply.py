# Multiples two numbers with recursion

class Multiplier():

    def multiply(self, x, y):
        if y == 0:
            return 0
        if y > 0:
            return (x + self.multiply(x, y - 1))
        if y < 0:
            return -self.multiply(x, -y)


import unittest

class MultiplyTest(unittest.TestCase):

    def test_multiply(self):
        multy = Multiplier()
        print("Testing positve multiplication: ", 2, 4, 8)
        self.assertEqual(multy.multiply(2, 4), 8)

    def test_multiply_one_negative(self):
        multy = Multiplier()
        print("Testing negative multiplication: ", -5, 3, -15)
        self.assertEqual(multy.multiply(-5, 3), -15)

    def test_multiply_both_negative(self):
        multy = Multiplier()
        print("Testing negative multiplication: ", -1, -10, 10)
        self.assertEqual(multy.multiply(-1, -10), 10)

if __name__ == '__main__':
    unittest.main()