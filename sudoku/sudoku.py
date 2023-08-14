# Create a program that generates a random Sudoku puzzle. 
# Handle any exceptions that might occur during the puzzle generation process.

import random

def print_sudoku(sudoku):
    for row in sudoku:
        print("".join("["+str(num)+"]" if num != 0 else "[ ]" for num in row))
    print()

def is_valid(sudoku, row, col, num):
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if sudoku[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(sudoku, row, col, num):
                        sudoku[row][col] = num
                        if solve_sudoku(sudoku):
                            return True
                        sudoku[row][col] = 0
                return False
    return True

def generate_sudoku():
    sudoku = [[0] * 9 for _ in range(9)]
    solve_sudoku(sudoku)
    
    # Remove some numbers to create the puzzle
    num_to_remove = random.randint(30, 45)
    cells = [(row, col) for row in range(9) for col in range(9)]
    random.shuffle(cells)
    
    for _ in range(num_to_remove):
        row, col = cells.pop()
        removed_num = sudoku[row][col]
        sudoku[row][col] = 0
        
        # Check if the puzzle is still solvable with the number removed
        temp_sudoku = [row[:] for row in sudoku]
        solutions = [0]
        solve_sudoku(temp_sudoku)
        solutions[0] = temp_sudoku
        
        if solutions[0] is None:
            # If removing the number makes the puzzle unsolvable, put it back
            sudoku[row][col] = removed_num
    
    return sudoku

if __name__ == "__main__":
    puzzle = generate_sudoku()
    print("Generated Sudoku Puzzle:")
    print_sudoku(puzzle)   