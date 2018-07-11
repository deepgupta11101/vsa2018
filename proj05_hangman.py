# Name:
# Date:


# proj05: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
print "Welcome to our Hangman game!"
print ""
want = int(raw_input("How many letters would you like your word to be? "))
print ""
word=choose_word(wordlist)
while len(word)!=want:
    word = choose_word(wordlist)
guessesLeft = int(raw_input("How many guesses would you like to have for this game? "))
print ""
word = list(word)
unusedLetters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
revealed= []
for i in range (len(word)):
    revealed.append("_")
print "I am thinking of a word that is", len(word), "letters long."
while guessesLeft>0 and revealed.count("_")>0:
    x = 1
    print "---------------------------------------"
    print "You have", guessesLeft,"guesses remaining."
    print ""
    print "Available letters: " + ' '.join(unusedLetters)
    print ""

    while x == 1:
        guess=raw_input("Please guess a letter: ")
        print ""
        if guess in unusedLetters:
            x = 0


    if guess not in unusedLetters:
        print "Your guess was not valid. Please try again"
    counter =0
    if guess in word:
        for i in range (len(word)):
            if word[counter]==guess:
                revealed[counter]=guess
            counter+=1
        print "Good guess: " + ' '.join(revealed)
    else:
        guessesLeft-=1
        print "Oops! That letter is not in my word: " + ' '.join(revealed)
    unusedLetters.remove(guess)
if guessesLeft>0:
    print "Congrats, you won! You had", guessesLeft, "guesses remaining!"
else:
    print "Sorry, you did not guess my word in the number of guesses. The word was", word
