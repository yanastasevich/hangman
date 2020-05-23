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
print (random_word)


def print_lanes(word):
    word_length = len (word);
    print (' _ ' * word_length)


def word_input (word):
    count = 0
    guess_word = ' '
    while count < len (word):
        char_guess = input ("> ")
        guess_word += char_guess
        count += 1
    else:
        print ("You've reached the limit of inputs with this word")
    return guess_word


# g_word - is a guess word and r_word is for real word
def word_guess(g_word, r_word):
    g_pos = 0
    r_pos = 0
    while g_pos < len (g_word) and r_pos < len (r_word):
          if g_word[g_pos] == r_word [r_pos]:
              g_pos += 1
          r_pos += 1
    return g_pos == len (g_word)



print_lanes (random_word)
a = word_input (random_word)
word_guess (a, random_word)
