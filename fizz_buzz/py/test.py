import fizz_buzz
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_return_fizz_buzz(self):
        fizz_buzzer = fizz_buzz.FizzBuzz([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
        list_fizz_buzz = fizz_buzzer.returnFizzBuzz()
        self.assertEqual(list_fizz_buzz, [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14, "fizz buzz"])

if __name__ == "__main__":
    unittest.main()