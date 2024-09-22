import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O

def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] is EMPTY}

def result(board, action):
    i, j = action
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid action")

    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None

def terminal(board):
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)

def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

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
