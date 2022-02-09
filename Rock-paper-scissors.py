#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
#print out a message of congratulations to the winner, and ask if the players want to start a new game)

def Game():
    
    
    winner = "no one"
    while True:    
            
        player1 = input("Player 1 - Choose Rock, Scissors or Paper: ")
        player2 = input("Player 2 - Choose Rock, Scissors or Paper: ")    
           
            
        if player1 == "rock" and player2 == "paper":
                winner = "Player 2"
        elif player1 == "rock" and player2 == "scissors":
                winner = "Player 1"
        
        if player1 == "paper" and player2 == "scissors":
                winner = "Player 2"
        elif player1 == "paper" and player2 == "rock":
                winner = "Player 1"
        
        if player1 == "scissors" and player2 == "rock":
                winner = "Player 2"
        elif player1 == "scissors" and player2 == "paper":
                winner = "Player 1"
        elif player1 == player2:
                winner = "It's a tie"
        
        print("Winner is " + winner)
            
        nextgame = input("Do you want to play again? Yes / No: ")
            
        if nextgame == "No":
            winner = "end game"
            print("Thanks for playing")
            break
        elif nextgame == "yes":
            winner = "no one"
            
Game()