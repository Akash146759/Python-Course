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
