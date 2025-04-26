<<<<<<< HEAD
import tkinter as tk
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        self.board = [" "] * 9  # Board representation
        self.current_turn = "X"  # Player starts first
        self.buttons = []  # Store buttons
        
        self.create_ui()  # Initialize GUI
    
    def create_ui(self):
        """ Create the game board UI """
        for i in range(9):
            btn = tk.Button(self.root, text=" ", font=("Arial", 20), height=2, width=5,
                            command=lambda i=i: self.player_move(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)
        
        self.status_label = tk.Label(self.root, text="Player X's Turn", font=("Arial", 14))
        self.status_label.grid(row=3, column=0, columnspan=3)
        
        reset_btn = tk.Button(self.root, text="Restart", font=("Arial", 14),
                              command=self.reset_game)
        reset_btn.grid(row=4, column=0, columnspan=3)
    
    def player_move(self, index):
        """ Handle player move """
        if self.board[index] == " " and self.current_turn == "X":
            self.board[index] = "X"
            self.buttons[index].config(text="X", state=tk.DISABLED)
            
            if self.check_winner("X"):
                self.status_label.config(text="🎉 Player X Wins!")
                self.disable_board()
                return
            
            if " " not in self.board:
                self.status_label.config(text="🤝 It's a Tie!")
                return
            
            self.current_turn = "O"
            self.status_label.config(text="AI's Turn")
            self.root.after(500, self.ai_move)  # AI moves after a slight delay
    
    def ai_move(self):
        """ AI's turn to make a move """
        empty_positions = [i for i in range(9) if self.board[i] == " "]
        if empty_positions:
            index = random.choice(empty_positions)  # AI chooses a random empty spot
            self.board[index] = "O"
            self.buttons[index].config(text="O", state=tk.DISABLED)
            
            if self.check_winner("O"):
                self.status_label.config(text="🤖 AI Wins!")
                self.disable_board()
                return
            
            self.current_turn = "X"
            self.status_label.config(text="Player X's Turn")
    
    def check_winner(self, player):
        """ Check if the given player has won """
        win_conditions = [(0,1,2), (3,4,5), (6,7,8),
                          (0,3,6), (1,4,7), (2,5,8),
                          (0,4,8), (2,4,6)]
        return any(self.board[a] == self.board[b] == self.board[c] == player for a, b, c in win_conditions)
    
    def disable_board(self):
        """ Disable all buttons after game over """
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)
    
    def reset_game(self):
        """ Reset the game board """
        self.board = [" "] * 9
        self.current_turn = "X"
        self.status_label.config(text="Player X's Turn")
        
        for btn in self.buttons:
            btn.config(text=" ", state=tk.NORMAL)

# Run the game
root = tk.Tk()
app = TicTacToe(root)
root.mainloop()
=======
#Implementation of Two Player Tic-Tac-Toe game in Python.

''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now we'll write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()
>>>>>>> c4323b7f6363cbd3fa02e1fe72caae982605e624
