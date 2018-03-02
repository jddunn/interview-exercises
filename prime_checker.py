# Prime number checker

class PrimeChecker():

    def is_prime_fast(self, number):
        # Using list comprehension
        return(all([number % i != 0 for i in range(2, number)]))

    def is_prime(self, number):
            for i in range(2,number):
                if (number % i) == 0:
                   return False
            return True


import unittest
import time

class PrimesTestCase(unittest.TestCase):

    def test_is_prime_fast(self):
        number = 15485867   
        print("Testing " + str(number) + " for primality with list comprehension.")
        start = time.time()
        prime_checker = PrimeChecker()
        self.assertTrue(prime_checker.is_prime_fast(number))
        end = time.time()
        duration = end - start
        print("Processing duration: " + str(duration) +" seconds.")

    def test_is_prime(self):
        number = 15485867   
        print("Testing " + str(number) + " for primality with for loop.")
        start = time.time()
        prime_checker = PrimeChecker()
        self.assertTrue(prime_checker.is_prime(number))
        end = time.time()
        duration = end - start
        print("Processing duration: " + str(duration) +" seconds.")

if __name__ == '__main__':
    unittest.main()