import numpy as np
#import pandas as pd
#from pandas import DataFrame
#import matplotlib.pyplot as plt
#from IPython.display import display
from random_word import RandomWords

################
#Prep Functions#
################


def pick_random_word():
    # Instantiate randomizer
    r = RandomWords()

    true_word = r.get_random_word(
        hasDictionaryDef="true", includePartOfSpeech="noun,verb,adjective", minDictionaryCount=3, minLength=5, maxLength=5)

    while true_word == None or '-' in true_word:
        true_word = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb,adjective",
                                      minDictionaryCount=3, minLength=5, maxLength=5).upper()
    else:
        #         print(f'Word is: {true_word}')
        return true_word


def ask_user_input(guru=None):
    while True:
        guru = input("Guess a 5-letter Word :")
        if type(guru) != str or len(guru) != 5:
            print('Invalid Entry')
            continue
        else:
            return guru.upper()


###############
#Main Function#
###############


def play_wordle():
    # Initialize Answer
    ans_word = "hello"
    ans_arr = np.array(list(ans_word.upper()))
    ans_idx = [[item, idx, None] for idx, item in enumerate(ans_arr)]
    # print(ans_idx)

    # Initialize Variables
    attempt = 0

    while attempt < 6:
        num_G = 0
        num_Y = 0
        # Ask User for Input
        guess_word = ask_user_input()
        guess_arr = np.array(list(guess_word.upper()))
        guess_idx = [[item, idx, None] for idx, item in enumerate(guess_arr)]
        # print(guess_idx)

        #########################
        #Compare Guess to Answer#
        #########################

        # 'matched' is the letter that matches
        matched = []
        # 'existing' is the letter that is already used for comparison
        existing = []
        # 'matching' is the letter that matches' number order (0~4)
        matching = np.where(ans_arr == guess_arr)[0]
        # print(len(matching))
        # print(matching):

        # append letters that match to 'matched'
        for item in matching:
            matched.append(guess_idx[item][0])
            guess_idx[item][2], ans_idx[item][2] = "G", "G"
        # print(matched)
        # print(guess_idx)
        # print(ans_idx)

        # search for remaining letters that are in wrong position but in the word
        rem_guess = [item for item in guess_idx if item[2] != "G"]
        rem_ans = [item for item in ans_idx if item[2] != "G"]
        # print(rem_guess, rem_ans)

        for guess in rem_guess:
            for ans in rem_ans:
                if guess[0] == ans[0]:
                    if list(ans_arr).count(guess[0]) > (matched.count(guess[0]) + existing.count(guess[0])):
                        existing.append(guess[0])
                        guess[2], ans[2] = 'Y', 'Y'

                    else:
                        continue

        # find the number of yellows in the guess_idx
        for item in guess_idx:
            if item[2] == 'Y':
                num_Y += 1
        # find the number of greens in the guess_idx
        for item in guess_idx:
            if item[2] == 'G':
                num_G += 1
        #print(num_G, num_Y)

        # Create win/fail condition
        if guess_word.upper() == ans_word.upper():
            print('##############################################################')
            print(f'       HURRAY THE WORD WAS: {ans_word.upper()} ')
            print('##############################################################')
            print('YOU ARE A HUMAN GENIUS! YOU SHOULD BE FEARED AND RESPECTED!!!')
            print('Give yourself a pat on the shoulder :)')
            print("That student debt is finally paying off!!!")
            print("WANNA PLAY AGAIN?")
            break
        else:
            attempt += 1
            print('##############################################################')
            print(f'            Correct Letters in Position: {num_G}')
            print('##############################################################')
            print(f'            Correct Letters in Word: {num_Y}')
            print('##############################################################')
            print(f'            Remaining Attempts: {10-attempt}')
            print('##############################################################')

            if attempt == 10:
                print(
                    f'Sorry, gotta read more BOOKS! The word was obviously {ans_word.upper()}')
                break


play_wordle()
