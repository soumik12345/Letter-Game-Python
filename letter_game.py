import random
import os
import sys

words = [
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon'
]

def clear():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')


def draw(bad_guesse,good_guesses,secret_word):
    clear()
    print("Strikes: {}/7".format(len(bad_guesses)))
    print('')
    for letter in bad_guesses:
        print(letter,end=' ')
    print('\n\n')
    for letter in secret_word:
        if letter in good_guesses:
            print(letter,end='')
        else:
           print('_',end='')
    print('')
    


def guesses(bad_guesses,good_guesses):
    while True:
        guess=input("Guess a letter: ").lower()
        if len(guess)!=1:
            print("You can only guess one letter at a time.")
        elif guess in bad_guesses or guess in good_guesses:
            print("You have already guessed that letter.")
        elif not guess.isalpha():
            print("You can only guess letters.")
        else:
            return guess


def play(done):
    clear()
    secret_word=random.choice(words)
    bad_guesses=[]
    good_guesses=[]
    while True:
        draw(bad_guesse,good_guesses,secret_word)
        guess=guesses(bad_guesses,good_guesses)
        if guess in secret_word:
            good_guesses.append(guess)
            found=True
            for letter in secret_word:
                if letter not in good_guesses:
                    found=False
            if found:
                print("You win!\nThe secret word was {}.".format(secret_word))
        else:
            bad_guesses.append(guess)
            if len(bad_guesses)==7:
                draw(bad_guesse,good_guesses,secret_word)
                print("You lose!\nThe secret word was {}.".format(secret_word))
                done=True
        if done:
            play_again=input("Play again???(Y/N) ").lower()
            if play_again!='n':
                return (done=False)
            else
                sys.exit()



def welcome():
    start=input("Press enter to start the game or enter Q to exit: ").lower()
    if start=='q':
        print("Bye")
        sys.exit()
    else
        return True



print("Welcome to Letter Guess.")
done=False
while True:
    clear()
    welcome()
    paly(done)
