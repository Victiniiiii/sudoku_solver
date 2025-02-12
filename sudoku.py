import random

def print_board(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-" * 21)
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")
            print(board[row][col], end=" ")
        print()

def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    for r in range(9):
        if board[r][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def copy_board(board):
    return [row[:] for row in board]

def generate_sudoku(difficulty):
    board = [[0] * 9 for _ in range(9)]
    for _ in range(10):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if is_valid(board, row, col, num):
            board[row][col] = num
    solve(board)
    full_solution = copy_board(board)
    clues = {"easy": 40, "medium": 30, "hard": 20}[difficulty]
    positions = random.sample(range(81), 81 - clues)
    for pos in positions:
        board[pos // 9][pos % 9] = 0
    return board, full_solution

def play_sudoku(board, solution):
    lives = 3
    while lives > 0:
        print_board(board)
        try:
            row, col, num = map(int, input("Enter row, column, and number (1-9) separated by spaces: ").split())
            if board[row-1][col-1] != 0:
                print("Cell already filled. Try a different cell.")
            elif solution[row-1][col-1] != num:
                print("Incorrect move. You lost a life!")
                lives -= 1
            else:
                board[row-1][col-1] = num
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row, column, and number values.")
        
        if all(board[row][col] != 0 for row in range(9) for col in range(9)):
            print("Congratulations! You solved the Sudoku!")
            return
    print("Game over! You ran out of lives.")

def main():
    print("Welcome to Sudoku!")
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    while difficulty not in {"easy", "medium", "hard"}:
        difficulty = input("Invalid choice. Choose difficulty (easy, medium, hard): ").lower()
    board, solution = generate_sudoku(difficulty)
    play_sudoku(board, solution)

if __name__ == "__main__":
    main()
