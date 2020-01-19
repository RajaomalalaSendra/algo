from count import CountVowelsAndConsonnants

if __name__ == "__main__":
    text = input(">> ")
    counts = CountVowelsAndConsonnants(text)
    num_consonants = counts.countConsonnants()
    num_vowels = counts.countVowels()
    print("""Numbers of consonnants in this text: %d.
Numbers of vowels in this text: %d.""" % (num_consonants, num_vowels))