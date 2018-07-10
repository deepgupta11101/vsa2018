# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random
import math

startNewGame = False
print "Welcome to our guessing game!"
print "You get to choose the highest number of the range. My number will be between 1 and the next number you type."
upper = int(raw_input("Please enter the number you want for the upper bound."))
my_num = random.randint(1, upper)
guesses = 0
done = False
allowedGuesses = int(math.log(upper, 2))+1
print "You have",allowedGuesses,"chances to guess the random number."
while done == False and guesses <= allowedGuesses:
    if startNewGame == True:
        upper = int(raw_input("Please enter the number you want for the upper bound."))
        my_num = random.randint(1, upper)
        allowedGuesses = int(math.log(upper, 2)) + 1
        print "You have", allowedGuesses, "chances to guess the random number."
        startNewGame = False
    num = raw_input("Guess a number or enter END to quit the game.")
    if num == "END":
        print "Thanks for playing. You had guessed", guesses, "times before you quit."
        done = True
    elif int(num) < my_num:
        guesses += 1
        print "Your number is too low! You have", allowedGuesses-guesses, "guesses remaining."
    elif int(num) > my_num:
        guesses += 1
        print "Your number is too high! You have", allowedGuesses-guesses, "guesses remaining."
    else:
        guesses += 1
        print "Congrats on guessing the number! You used", guesses, "guesses to win the game."
        done = True
        ans = raw_input("If you want to play again, type AGAIN and enter.")
        if ans == "AGAIN":
            guesses = 0
            done = False
            startNewGame = True
if guesses > 6:
    print "Thanks for playing, but you reached the maximum number of guesses before you won. The correct answer was", my_num