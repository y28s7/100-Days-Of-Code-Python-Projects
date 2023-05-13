import pandas

nato_alphabet_raw = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in nato_alphabet_raw.iterrows()}

def generate_phonetic():
    inputted_word = input("Input a word: ").upper()
    try:
        nato_alphabet_words = ", ".join([nato_alphabet[letter] for letter in inputted_word])
    except KeyError:
        print("Please enter only letters.")
        generate_phonetic()
    else:
        print(f"Your word in the NATO Phonetic Alphabet is: {nato_alphabet_words}")
generate_phonetic()
