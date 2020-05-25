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
    word_length = len (word);
    return ' _ ' * word_length


# the guess_count should be fixed
# a separate mathod for it makes sense
# a method that checks for the guess counts
# i have to think about it tonight
def input_check_word(word):
    guess_pos = 0
    guess_word = ' '
    guess_count = 0
    while guess_pos < len (word) and guess_count <= 3:
        for t in word:
            char_guess = input ("> ")
            if char_guess == t:
                guess_word += char_guess
                guess_pos += 1
                guess_count += 1

        else:
            print ("Oops, you're hanged.\n")
            print ("Start again!\n")
            start()
    print ("Congratulations! You've guessed the whole letter!")
    return guess_word


def start():
    print ("""Welcome to Hangman!
A game where you have to guess the letters of the word!
You have three attempts to guess.\n""")

    print (f"The random word today is {random_word}")
    print (f"{print_lanes(random_word)} \n")
    print (f"Let's start with the guessing!")
    print (input_check_word(random_word))



start()
