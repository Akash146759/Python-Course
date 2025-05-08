import random

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = list(theBoard.keys())

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def checkWin(board, turn):
    win_conditions = [
        ['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'],  # rows
        ['7', '4', '1'], ['8', '5', '2'], ['9', '6', '3'],  # columns
        ['7', '5', '3'], ['1', '5', '9']  # diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            printBoard(board)
            print("\nGame Over.\n")
            print(f"**** {turn} won! ****")
            return True
    return False

def computerMove(board):
    available_moves = [key for key in board_keys if board[key] == ' ']
    return random.choice(available_moves)

def game():
    turn = 'X'  # User plays as 'X', Computer as 'O'
    count = 0

    while True:
        printBoard(theBoard)
        
        if turn == 'X':
            move = input("It's your turn, X. Move to which place? ")
        else:
            print("Computer's turn...")
            move = computerMove(theBoard)

        if move in theBoard and theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("Invalid move. Try again.")
            continue
        
        if count >= 5 and checkWin(theBoard, turn):
            break

        if count == 9:
            print("\nGame Over.\nIt's a Tie!")
            break

        turn = 'O' if turn == 'X' else 'X'

    restart = input("Do you want to play again? (y/n) ")
    if restart.lower() == 'y':
        for key in board_keys:
            theBoard[key] = ' '
        game()

if __name__ == "__main__":
    game()
