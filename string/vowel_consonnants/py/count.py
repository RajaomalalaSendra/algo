# Count the number of vowel and consonants
class CountVowelsAndConsonnants:
    """This class is used to:
            - count the number of the vowels.
            - count the number of the consonnants."""
    def __init__(self, text):
        self.text = text.lower()
        self.vowels = "aeiouy"
        self.consonants = "bcdfghjklmnpqrstvwxz"

    def countVowels(self):
        countvowels = 0
        
        for i in range(0, len(self.text)):
            if(self.text[i] in self.vowels):
                countvowels += 1
        
        return countvowels
                
    
    def countConsonnants(self):
        countConsonants = 0

        for j in range(0, len(self.text)):
            if(self.text[j] in self.consonants):
                countConsonants += 1
        
        return countConsonants