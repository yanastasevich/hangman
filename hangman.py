import random

play_words = {
    'polycarbonate',
    'cat',
    'sugar',
    'junk',
    'stuff',
    'princess',
    'death'
}


random_word =  random.choice(tuple (play_words))


def print_lanes(word):
    lanes = []
    word_length = len (word)
    for i in range (len (word)):
        lanes.extend ("_")
    print (*lanes, sep = " ")
    return lanes


def input_char(word):
     char_guess = input ("> ")
     return char_guess


def check_char(word):
    char_input = input_char(random_word)

    if char_input in word:
        return True
    else:
        return False


def start():
    print ("""Welcome to Hangman!
A game where you have to guess the letters of the word!
You have three attempts to guess.\n""")

    print (f"The random word today is {random_word}\n")
    print_lanes(random_word)
    print (f"Let's start with the guessing!")
    print (check_char(random_word))



start()
