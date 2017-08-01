# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().upper())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!


a = 'Player 1'
b = 'Player 2'

def get_input(currentPlayer):
    while True:
        letter = raw_input('Enter a letter: ')
        letter = letter.upper()
        print currentPlayer,' says letter:',letter
        if letter in string.ascii_letters:
            return letter
        else:
            print letter, 'is not a letter'
            print
            
              
def change_player(currentPlayer):
    if currentPlayer == a:
        return b
    else:
        return a


def check_word(word,currentPlayer):
    length = len(word)
    
    if word in wordlist and length>3:
        print currentPlayer,'loses because word ',word, 'is a word!'
        return False
    else:
        for words in wordlist:
            if words[:length]==word:
#                print 'words[:length]', words[:length],'word',word
                return True
        if word not in wordlist:
            print currentPlayer,' loses because no word begins with ',word,'!'
            return False           



'''    
def test_check_word():
    print 'check_word2(ab)'
    check_word2('ab','Player1')
    raw_input()
    print 'check_word2(aba)'
    check_word2('aba','Player1')
    raw_input()
    print 'check_word2(aah)'
    check_word2('aah','Player1')
    raw_input()
    print 'check_word2(aahe)'
    check_word2('aahe','Player1')
    raw_input()
    print 'check_word2(q)'
    check_word2('q','Player1')
    raw_input()
    print 'check_word2(qz)'
    check_word2('qz','Player1')
    raw_input()
    print 'check_word2(aahed)'
    check_word2('aahed','Player1')
    raw_input()
'''    
    
def ghost():
    print 'Welcome to Ghost!'
    word = ''
    currentPlayer = a
    print currentPlayer,' goes first'
    

    
    while True:
        letter = get_input(currentPlayer)
        word = word + letter
        print
        print 'Current word fragment: ',word
        if not check_word(word,currentPlayer):
            break
        
        currentPlayer = change_player(currentPlayer)
        print currentPlayer,' turn.'
        if letter == '.':
            break
                

if __name__ == '__main__':
    ghost()                        
    
