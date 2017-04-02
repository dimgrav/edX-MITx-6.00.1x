# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
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
	


# Problem #1: Scoring a word
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # inital word score and letters sum score
    wscore = 0
    lscore = 0
    
    # calculate letters sum score
    for letter in word:
        if letter in SCRABBLE_LETTER_VALUES.keys():
            lscore += SCRABBLE_LETTER_VALUES[letter]
            
    # calculate word score
    if len(word) == n:
        wscore = lscore*n + 50
    else:
        wscore = lscore*len(word)
    
    return wscore

# Problem #2
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

# Problem #2
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

# Problem #2
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # create hand copy    
    updated = hand.copy()
    wordlen = 0
    
    # remove letters used in word
    for letter in updated:
        if letter in word:
            updated[letter] = updated.get(letter, 0) - word.count(letter)
            wordlen += word.count(letter)
    if wordlen == len(word):
        hand = updated
        
    return hand

# Problem #3
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if word in wordList:
        for letter in word:
            if letter in hand.keys() and word.count(letter) <= hand[letter]:
                return True
            else:
                return False
    else:
        return False
       

# Problem #4
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    length = 0
    
    for letter in hand:
        length += hand[letter]
    
    return length



def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    
    total = 0
#    updated = hand.copy()
    while calculateHandlen(hand) > 0:
        # Display the hand
        print("Current hand: ", end = "")
        displayHand(hand)
        # Ask user for input
        word = str(input('Enter word, or a "." to indicate that you are finished: '))
        if word == ".":
            return "Goodbye! Total score: " + str(total) + " points."
            break
       
        else:
            if isValidWord(word, hand, wordList) == False:
                # Reject invalid word
                print("Invalid word, please try again.")
                print()
            else:
                total += getWordScore(word, n)
                print(' " ' + str(word) + ' " ' + " earned " + str(getWordScore(word, n)) + " points. Total: " + str(total) + " points")
                # Update the hand
                updateHand(hand, word)
        
                if all(value == 0 for value in hand.values()):
                    break
                
    # Game is over (user entered a '.' or ran out of letters)
    return "Run out of letters. Total score: " + str(total) + " points."

# Problem #5
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    counter = 0
    
    while True:
        start = str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
        
        if start not in "nre":
            print("Invalid command.")
        elif start == "e":
            break
        elif start == "n":
            
            # deals a hand
            deal = dealHand(HAND_SIZE)
            counter += 1
            # plays the hand
            playHand(deal, wordList, HAND_SIZE)
        elif start == "r":
            if counter == 0:
                print("You have not played a hand yet. Please play a new hand first!")
            else:
                playHand(deal, wordList, HAND_SIZE)
   

# Build data structures used for entire session and play game

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
