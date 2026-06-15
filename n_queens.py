# Function to print the chessboard
def print_board(board, n):

    for row in board:
        print(" ".join(row))

    print()


# Function to check if queen can be placed safely
def is_safe(board, row, col, n):

    # Check same column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False

        i -= 1
        j -= 1

    # Check right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False

        i -= 1
        j += 1

    return True


# Backtracking function
def solve_n_queens(board, row, n):

    # If all queens placed
    if row == n:
        print("Solution Found:\n")
        print_board(board, n)
        return True

    # Try placing queen in each column
    for col in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = "Q"

            if solve_n_queens(board, row + 1, n):
                return True

            # Backtrack
            board[row][col] = "."

    return False


# Main program
n = 4

# Create empty board
board = [["." for i in range(n)] for j in range(n)]

# Solve problem
if not solve_n_queens(board, 0, n):
    print("No solution exists.")