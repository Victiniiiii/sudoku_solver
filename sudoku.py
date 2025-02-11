import random

# A function to print the Sudoku board nicely
def print_board(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-" * 21)  # Print a horizontal line between 3x3 sections
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")  # Print a vertical line between 3x3 sections
            print(board[row][col], end=" ")
        print()

# A function to check if a move is valid
def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False
    # Check column
    for r in range(9):
        if board[r][col] == num:
            return False
    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True

# A function to solve the board (backtracking algorithm)
def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0  # Backtrack
                return False
    return True

# A function to generate a solvable Sudoku puzzle
def generate_sudoku():
    board = [[0] * 9 for _ in range(9)]
    for _ in range(10):  # Add 10 random valid numbers to start the puzzle
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if is_valid(board, row, col, num):
            board[row][col] = num
    return board

# A function to prompt the user for input
def play_sudoku(board):
    while True:
        print_board(board)
        try:
            row, col, num = map(int, input("Enter row, column, and number (1-9) separated by spaces: ").split())
            if board[row-1][col-1] != 0:
                print("Cell already filled. Try a different cell.")
            elif not is_valid(board, row-1, col-1, num):
                print("Invalid move. Try again.")
            else:
                board[row-1][col-1] = num
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row, column, and number values.")
        
        # Check if the puzzle is solved
        if all(board[row][col] != 0 for row in range(9) for col in range(9)):
            print("Congratulations! You solved the Sudoku!")
            break

# Main function to set up and play the game
def main():
    board = generate_sudoku()  # Generate a new Sudoku puzzle
    print("Welcome to Sudoku!")
    play_sudoku(board)

if __name__ == "__main__":
    main()
