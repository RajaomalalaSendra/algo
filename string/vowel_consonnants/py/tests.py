import unittest
from count import CountVowelsAndConsonnants


class TestCountVowelsAndConsonnants(unittest.TestCase):
    def test_count_vowels(self):
        count_vowels_and_consonnants = CountVowelsAndConsonnants("abcababb")
        countVowels = count_vowels_and_consonnants.countVowels()
        self.assertEqual(countVowels, 3)
        
    def test_count_consonants(self):
        count_vowels_and_consonnants = CountVowelsAndConsonnants("abcababb")
        countConsonants = count_vowels_and_consonnants.countConsonnants()
        self.assertEqual(countConsonants, 5)

if __name__ == "__main__":
    unittest.main()