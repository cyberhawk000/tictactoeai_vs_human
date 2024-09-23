"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #Determines whose turn to play, it counts X and O on the board
    x_moves = sum(row.count(X) for row in board)
    o_moves = sum(row.count(O) for row in board)
    return O if x_moves > o_moves else X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #This functoin returns all possible moves a player can make.
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #This function returns a new board after applying action.
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid action")
    
    next_board = [row.copy() for row in board]  # Deep copy of the board
    next_board[action[0]][action[1]] = player(board)
    return next_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # This funtion check all possible wining combinations
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #max_value and max_value to calculate the best possible outcomr

    if terminal(board):
        return None

    current_player = player(board)

    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    if current_player == X:
        best_value = -math.inf
        best_move = None
        for action in actions(board):
            move_value = min_value(result(board, action))
            if move_value > best_value:
                best_value = move_value
                best_move = action
        return best_move
    else:
        best_value = math.inf
        best_move = None
        for action in actions(board):
            move_value = max_value(result(board, action))
            if move_value < best_value:
                best_value = move_value
                best_move = action
        return best_move
