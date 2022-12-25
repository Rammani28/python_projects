import pandas

df = pandas.read_csv('NATO_phonetic_alphabet.csv')
alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    try:
        word = input("Enter a word: ").upper()
        output_list = [alphabet_dict[letter] for letter in word]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()