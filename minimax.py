"""
This function changes the board into 1, -1, and 0s from X, O, and blanks.
:param board: the game board as a 2D array
:return: a 2D array consisting of 1, -1, and 0s
"""
def change_board(board):
    return [
        [(cell == "O") - (cell == "X") for cell in row]
        for row in board
    ]

"""
This function determines which cells are empty and returns a list of all of the empty cells in the game board.
:param board: the game board as a 2D array
:return: list of empty cells in board
"""
def empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

"""
This function determines whether the game is complete through either a win or draw.
:param board: the game board as a 2D array
:return: boolean indicating whether the game is over
"""
def game_over(board):
    return (evaluate(board) == 10 or evaluate(board) ==-10 or not empty_cells(board))
    
lines = (
    (0, 0, 1, 1, 2, 2),
    (0, 2, 1, 1, 2, 0),
    (0, 0, 0, 1, 0, 2),
    (1, 0, 1, 1, 1, 2),
    (2, 0, 2, 1, 2, 2),
    (0, 0, 1, 0, 2, 0),
    (0, 1, 1, 1, 2, 1),
    (0, 2, 1, 2, 2, 2)
)

"""
This function evaluates the board to determine what the current score is.
:param board: the game board as a 2D array
:return: int value representing the score (-10 for a player win, 10 for a computer win, and 0 for no win)
"""
def evaluate(board):
    def iswin(line):
        arow, acol, brow, bcol, crow, ccol = line
        if board[arow][acol] == board[brow][bcol] == board[crow][ccol]:
            return board[arow][acol]*10

    return next((win for win in map(iswin, lines) if win), 0)
    
"""This function uses a minimax algorithm to recursively determine the ending score for a move and pick the best move.
:param board: the game board as a 2D array
:param depth: the depth in the game tree, which decreases from 9 to 0 with each play.
:param player: int representing the computer (1) or human player (-1)
:return: tuple containing row, column, and score of the best move for the player
"""
def minimax(board, depth, player):
    best = (-1, -1, -11*player)

    if depth <= 0 or game_over(board):
        return (-1, -1, evaluate(board)) 

    for x, y in empty_cells(board):
        board[x][y] = player
        score = minimax(board, depth - 1, -player)[2]  # only get the score
        board[x][y] = 0
        if (player == 1) == (score > best[2]):
            best = (x, y, score)  # only inject x, y when move is best

    return best