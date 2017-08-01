# Problem Set 6: 6.00 Word Game II
# Name: 
# Collaborators: 
# Time: 
#

import random
import string
import time
import itertools

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code

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
        wordlist.append(line.strip().lower())
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

#def get_frequency_dict(sequence):
#    freq = {}
#    for x in sequence:
#        if x in freq.keys():
#            freq[x]=freq[x] + 1
#        else:
#            freq[x]=1
#    return freq


# (end of helper code)
# -----------------------------------


# Problem: Scoring a word

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    
    count = 0
    word = word.lower()
    for letter in word:
        if letter in SCRABBLE_LETTER_VALUES.keys():
            count += SCRABBLE_LETTER_VALUES[letter]
    if n == len(word):
        count += 50
                
    return count


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.
 
    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand


# Problem : Update a hand by removing letters

def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    newhand = hand.copy()
    for letter in word:
        if letter in newhand.keys() and newhand[letter]>0:
            newhand[letter] = newhand.get(letter)-1
    return newhand

# Problem : Test word validity

def is_valid_word(word, hand, POINTS_DICT):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """

    newhand = hand.copy()
   
    if word in POINTS_DICT.keys():
        for letter in word:
            if letter in newhand.keys() and newhand[letter]>0:
                newhand[letter] = newhand[letter]-1
            else:
                return False
   
        return True                     
    return False

# Problem : Computer Play

def get_words_to_points(word_list):
    """
    Return a dict that maps every word in word_list to its point value.
    """
    d = {}
    for word in word_list:
        score = get_word_score(word,0)
        d[word] = score
    return d
'''
def test():
    word_list = load_words()
    word_list=word_list
    print get_words_to_points(word_list)
'''

# Problem : Even Faster Computer Player

def get_word_rearrangements(word_list):
    """
    Return a dict that maps every word in word_list with string containing the
    letters of word in sorted order.
    """
    d={}
    for word in word_list:
        d[''.join(sorted(word))] = word

    return d

    
def pick_best_word(hand, POINTS_DICT):
    """
    Return the highest scoring word from points_dict that can be made with the
    given hand.

    Return '.' if no words can be made with the given hand.
    """

    newhand = []
    for letter in hand.keys():
        for j in range(hand[letter]):
            newhand.append(letter)
       
    bestWords = {}
    for key, value in POINTS_DICT.items():
        handOK = newhand[:]
        inputOK = True
        for letter in key:
            if letter not in handOK:
                inputOK = False

            elif letter in newhand:
                handOK.remove(letter)
        if inputOK:
            bestWords[key] = value

    if bestWords == {}:
        return '.'
            

    bestValue = 0
    bestKey = None
    for key, value in bestWords.items():
        if value > bestValue:
            
            bestValue = value
            bestKey = key

    return bestKey

#straightforward implementation

def pick_best_word_slower(hand, POINTS_DICT):
     bestWords = {}
     for key,value in POINTS_DICT.items():
        if is_valid_word(key, hand, POINTS_DICT):
            print key, value


def pick_best_word_faster_wrong(hand,d):
    """
    PSEUDOCODE:
    To find some word that can be made out of the letters in HAND:
        For each subset of S of the letters of HAND:
            Let w = (string containing the letters of S in sorted order)
            If w in d: return d[w]
    """
    
    local_hand = []
    sublist = []
    for letter in hand.keys():
        for j in range(hand[letter]):
            local_hand.append(letter)
    
    local_hand = ''.join(local_hand)
    hand_len = len(local_hand)
     
    while hand_len!= 0:
        substring = local_hand[:hand_len]
        sub_len = len(substring)
        j = 0
        while j < sub_len:
            w = substring[j:]
            sublist.append(w)
            j = j+1
        hand_len -= 1
        
    # sublist doesn t contain all combinations of possible words    
    result = []       
    for word in sorted(sublist):
        if word in d.keys():
            result.append(d[word])

    score = 0
    high_word = ''
    for x in result:
        if POINTS_DICT[x] > score:
            score = POINTS_DICT[x]
            high_word = x

    if score == 0:
        return '.'
    else:
        return high_word


def pick_best_word_faster(hand,d):
    """
    PSEUDOCODE:
    To find some word that can be made out of the letters in HAND:
        For each subset of S of the letters of HAND:
            Let w = (string containing the letters of S in sorted order)
            If w in d: return d[w]
    """
    score = 0
    high_word = ""
    perms = []
    attempts = 0
    local_hand = []

    # itertools.permutations is iterating for letters
    # that are zero count in the hash, dump the zeros
    # convert dict to list
    
    for k in hand.keys():
        if hand[k] > 0:
            for i in range(hand[k]):
                local_hand.append(k)

    print "local_hand: "
    print "\t",
    print local_hand
    print

    take = len(local_hand)
    
    # try for a bingo, then one less than a bingo, etc.
    while take != 0:
        perms = list(itertools.combinations(local_hand, take))
        take -= 1
    
        for letter_list in perms:
            attempts += 1
            sorted_word = ''.join(sorted(letter_list))

            if d.get(sorted_word, 0):         
                word = d[sorted_word]       
                if score < POINTS_DICT[word]:
                    score = POINTS_DICT[word]
                    high_word = word
                    print "word: %s  score: %d" % (high_word, score)

    print "------------------------------------------------------------"
             
    print "attempts: %d" % (attempts)
       
    if score < 1:
        return '.'
    else:
        return high_word
  

def get_time_limit(POINTS_DICT,k):
    """
    Return the time limit for the computer player as a function of the
    multiplier k.

    POINTS_DICT should be the same dictionary that is created by
    get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in POINTS_DICT:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
    end_time = time.time()
    # print 'end_time - start_time ',end_time - start_time
    return (end_time - start_time)*k

# Problem : Playing a hand

def play_hand(hand, POINTS_DICT):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    
    # time_limit = float(raw_input('Enter time limit, in seconds, for players: '))
    remaining_time = TIME_LIMIT
    print
    print 'Current Hand:',display_hand(hand)

    totalScore = 0
    

    while True:
# Problem : Time Limit        
        start_time = time.time()
        print 'Enter word, or a . to indicate that you finished: '
#       word = pick_best_word(hand, POINTS_DICT)
        word = pick_best_word_faster(hand,REARRANGE_DICT)
        print word
#        word = raw_input('Enter word, or a . to indicate that you finished: ')
        end_time = time.time()
        total_time = end_time - start_time
        remaining_time = remaining_time - total_time
        if remaining_time <=0:          
            print 'Total time exceeds {:.2f} seconds. You scored {:.2f} points.'.format(TIME_LIMIT,totalScore)
            break
        if total_time == 0:
            total_time == 1
        
        if word == '.':
            return 'Total score: {} points'.format(totalScore)
            
        elif is_valid_word(word, hand, POINTS_DICT):
            score = get_word_score(word, HAND_SIZE)
            score = score/total_time
#            score = float(score)
            totalScore += score
            hand = update_hand(hand,word)
            print 'It took %0.2f second to provide an answer.' % total_time
            if remaining_time <=0:          
                print 'Total time exceeds {:.2f} seconds. You scored {:.2f} points.'.format(TIME_LIMIT,totalScore)
                break
            print 'You have %0.2f seconds remaining.' % remaining_time
            print '{} earned {:.2f} points. Total: {:.2f} points'.format(word,score,totalScore)               
            
            print 'Current hand: ', display_hand(hand)
            
        else:
            print'Choose another word!'
                       
# Problem : Playing a game

def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
   
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), POINTS_DICT)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), POINTS_DICT )
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

# Build data structures used for entire session and play game

word_list = load_words()
POINTS_DICT = get_words_to_points(word_list)
REARRANGE_DICT = get_word_rearrangements(word_list)
TIME_LIMIT = get_time_limit(POINTS_DICT,1)

print 'Length of POINTS_DICT', len(POINTS_DICT)
print 'Length of REARRANGE_DICT', len(REARRANGE_DICT)

if __name__ == '__main__':    
    play_game(POINTS_DICT)

