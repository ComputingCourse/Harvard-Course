"""
Tic Tac Toe Player
"""

import math, copy

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
    x, o = 0, 0
    for row in board:
        for collum in row:
            if collum == "X":
                x +=1
            elif collum == "O":
                o +=1
    if x > o :
        return "O"
    else:
        return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i,j))
    return moves



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board = copy.deepcopy(board)
    i,j = action
    if not str(j) in "012" or not str(i) in "012":
        raise Exception
    if board[i][j] != EMPTY:
        raise Exception
    else:
        new_board[i][j] =   player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None
    if board[0][0] == board[1][1] and  board[0][0] == board[2][2] and board[0][0]!=EMPTY:
        winner = board[0][0]
    elif board[0][2] == board [1][1] and  board[0][2] == board[2][0]and board[0][2]!=EMPTY:
        winner = board[0][2]
    for i in range(3):
        if board[i][0] == board[i][1] and  board[i][0] == board[i][2]and board[i][0]!=EMPTY:
            winner = board[i][0]
        elif board[0][i] == board[1][i] and  board[0][i] == board[2][i]and board[0][i]!=EMPTY:
            winner = board[0][i]

    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    moves_left = 0
    if winner(board):
        return True
    for row in board:
        for collum in row :
            if collum == EMPTY:
                moves_left +=1
    if moves_left>0:
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v,min_value(result(board,action)))
    return v

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v,max_value(result(board,action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    elif player(board) == "X":
        plays = []
        for action in actions(board):
            plays.append([min_value(result(board,action)),action])

        return sorted(plays,key=lambda x: x[0],reverse=True)[0][1]

    elif player(board) == "O":
        plays = []
        for action in actions(board):
            plays.append([max_value(result(board,action)),action])

        return sorted(plays,key=lambda x: x[0])[0][1]








    while winning_state.parent != board.state:
        winning_state = winning_state.parent
    return winning_state.action

