# Looks correct: Create a row of three 0s, and replicate that row 3 times.
board = [[0, 0, 0]] * 3

# We place an 'X' in the top-left corner
board[0][0] = 'X'

# The Result:
print(board)
# [['X', 0, 0], 
#  ['X', 0, 0], 
#  ['X', 0, 0]]

# Allocates a brand new [0, 0, 0] list three separate times
safe_board = [[0, 0, 0] for _ in range(3)]

safe_board[0][0] = 'X'
print(safe_board)
# [['X', 0, 0], 
#  [0, 0, 0], 
#  [0, 0, 0]]