import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from IPython.display import display

################
#Prep Functions#
################


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
    ans_word = "Music"

    ans_arr = np.array(list(ans_word.upper()))

    ans_idx = [[item, idx, None] for idx, item in enumerate(ans_arr)]
    print(ans_idx)


pull test
play_wordle()
