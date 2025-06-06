player1 = input("Player 1: Rock, Paper, or Scissors? ").lower()
player2 = input("Player 2: Rock, Paper, or Scissors? ").lower()

if player1 == player2:
    print("It's a tie!")

if player1 == "rock":
    if player2 == "scissors":
            print("Player 1 wins! Rock crushes Scissors!")
    else:
            print("Player 2 wins! Paper covers Rock!")
elif player1 == "paper":
    if player2 == "rock":
            print("Player 1 wins! Paper covers Rock!")
    else:
            print("Player 2 wins! Scissors cut Paper!")
elif player1 == "scissors":
    if player2 == "paper":
            print("Player 1 wins! Scissors cut Paper!")
    else:
            print("Player 2 wins! Rock crushes Scissors!")
else:
    print("Invalid input! Please enter Rock, Paper, or Scissors.")
