#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
#then tell them whether they guessed too low, too high, or exactly right.
#Extras:
#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

randNumber = random.randint(1, 9)


def Game(randNumber):

    winner = "no one"
    count = 0
    while True:
        
        guess = int(input("Guess the number between 1 and 9 "))
        playAgain = "Type exit to quit"
        
        if guess > randNumber:
            winner = "no one"
            count += 1
            print("Guess is too high " + playAgain)
        elif guess < randNumber:
            winner = "no one"
            count += 1
            print("Guess iss too low " + playAgain)
        elif guess == randNumber:
            print("Guess is correct! ")
            count += 1
            playAgain = input("Type yes to play again or exit to quit ")
            winner = "user"        
        if playAgain == "exit":
            print("Thanks for playing")
            print("Your number of guesses was " + str(count))
            
            break
            
   
Game(randNumber)

