from tictactoe import player, actions, result, winner, terminal, terminal, utility

X = "X"
O = "O"
EMPTY = None

board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

# Test Player
# print(player(board))
# Test actions
# print(actions(board))
# Test result with actions
# print(actions(board).pop()) 
# print(result(board, actions(board).pop()))

# print(winner(board))

# print(terminal(board))

# Tests full game logic without minimax (2 computers playing random moves)


def printBoard():
    print(board[0])
    print(board[1])
    print(board[2])
    print("------------------")


printBoard()
while terminal(board) == False:
    board = result(board, actions(board).pop())
    printBoard()
    print(utility(board))
    
