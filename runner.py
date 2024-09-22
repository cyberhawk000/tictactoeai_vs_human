import importlib

# Load the tictactoe module dynamically
tictactoe = importlib.import_module('tictactoe')

def print_board(board):
    symbols = {None: " ", "X": "X", "O": "O"}
    for row in board:
        print("|".join([symbols[cell] for cell in row]))
        print("-" * 5)

def get_human_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) - 1
            return divmod(move, 3)
        print("Invalid input. Try again.")

def play_game():
    board = tictactoe.initial_state()
    print("Welcome to Tic-Tac-Toe!")
    
    while not tictactoe.terminal(board):
        print_board(board)

        if tictactoe.player(board) == tictactoe.X:  # Human's turn
            print("Your turn!")
            move = get_human_move()
            if move in tictactoe.actions(board):
                board = tictactoe.result(board, move)
            else:
                print("Invalid move. Try again.")
        else:  # AI's turn
            print("AI's turn!")
            move = tictactoe.minimax(board)
            board = tictactoe.result(board, move)

    print_board(board)

    if tictactoe.winner(board) == tictactoe.X:
        print("You win!")
    elif tictactoe.winner(board) == tictactoe.O:
        print("AI wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
