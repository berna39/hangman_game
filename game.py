import random
import string

from words import words_dictionary

#init a word
def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word


def hangman():
    valid_word = get_valid_word(words_dictionary) #retrieveing a valid word
    word_letters = set(valid_word) #get the word as a set
    alphabet = set(string.ascii_uppercase) #all ascii letter in eglish
    used_letters = set()  #letters already entered by the user

    #getting user's input
    user_letter = input('Guess a letter').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("you've alreadu used that character")
        else:
            print("worng character")




