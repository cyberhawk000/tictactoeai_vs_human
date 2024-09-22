import copy

# Constants for players and empty cell
X = "X"
O = "O"
EMPTY = None

# Returns the initial state of the board (3x3 grid).
def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Returns the player who has the next turn on a given board.
def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O

# Returns a set of all possible actions (i, j) available on the board.
def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] is EMPTY}

# Returns the board that results from making move (i, j) on the board.
def result(board, action):
    i, j = action
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid action")

    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board

# Returns the winner of the game, if there is one.
def winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None

# Returns True if the game is over, False otherwise.
def terminal(board):
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)

# Returns 1 if X has won, -1 if O has won, 0 otherwise.
def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

# Minimax algorithm to determine the optimal move for the current player.
def minimax(board):
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        value, move = max_value(board)
    else:
        value, move = min_value(board)

    return move

def max_value(board):
    if terminal(board):
        return utility(board), None

    value = float('-inf')
    best_action = None
    for action in actions(board):
        min_val = min_value(result(board, action))[0]
        if min_val > value:
            value = min_val
            best_action = action

    return value, best_action

def min_value(board):
    if terminal(board):
        return utility(board), None

    value = float('inf')
    best_action = None
    for action in actions(board):
        max_val = max_value(result(board, action))[0]
        if max_val < value:
            value = max_val
            best_action = action

    return value, best_action

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

