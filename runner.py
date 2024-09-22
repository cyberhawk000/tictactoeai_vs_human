from tictactoe import initial_state, player, actions, result, winner, terminal, minimax

# Print the current board state
def print_board(board):
    symbols = {None: " ", "X": "X", "O": "O"}
    for row in board:
        print("|".join([symbols[cell] for cell in row]))
        print("-" * 5)

# Translate board position from (i, j) to a human-friendly format (1-9)
def get_human_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) - 1
            return divmod(move, 3)
        print("Invalid input. Try again.")

# Run the game loop
def play_game():
    board = initial_state()
    print("Welcome to Tic-Tac-Toe!")
    
    while not terminal(board):
        print_board(board)
        
        if player(board) == "X":  # Human's turn
            print("Your turn!")
            move = get_human_move()
            if move in actions(board):
                board = result(board, move)
            else:
                print("Invalid move. Try again.")
        else:  # AI's turn
            print("AI's turn!")
            move = minimax(board)
            board = result(board, move)

    print_board(board)
    
    if winner(board) == "X":
        print("You win!")
    elif winner(board) == "O":
        print("AI wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
