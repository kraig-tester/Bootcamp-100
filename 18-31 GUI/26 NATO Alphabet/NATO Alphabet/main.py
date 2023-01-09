import pandas as pd

#TODO 1. Create a dictionary in this format:
nato_dataframe = pd.read_csv("nato_phonetic_alphabet.csv")

# data = nato_dataframe.to_dict()
nato_dict = {row.letter:row.code for (index, row) in nato_dataframe.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic()
    user_word = input("Input a word:").upper()

    try:
        nato_code = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_code)

generate_phonetic()