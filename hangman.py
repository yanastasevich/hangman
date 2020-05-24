import random

play_words = {
    ' polycarbonate',
    ' cat',
    ' sugar',
    ' junk',
    ' stuff',
    ' princess',
    ' death'
}


random_word =  random.choice(tuple (play_words))
print (random_word)


def print_lanes(word):
    word_length = len (word);
    print (' _ ' * word_length)


def word_guess(g_word, r_word):
    g_pos = 0
    r_pos = 0
    g_word = word_input (random_word)
    while g_pos < len (g_word) and r_pos < len (r_word):
          if g_word[g_pos] == r_word [r_pos]:
              g_pos += 1
          r_pos += 1
    return g_pos == len (g_word)


def input_check_word(word):
    count = 0
    guess_word = ' '
    while count < len (word):
        char_guess = input ("> ")
        guess_word += char_guess
        count += 1
    else:
        if guess_word == word:
            print ("You guessed the whole word")
        elif guess_word != word:
            print ("Oops, you're hanged")
    return guess_word




print_lanes (random_word)
#print (word_guess (word_input, random_word))
print (input_check_word (random_word))
