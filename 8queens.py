N = 8  

def printBoard(board):
    for row in board:
        print(" ".join('Q' if cell else '.' for cell in row))
    print()

def isSafe(board, row, col):
    for c in range(col):
        if board[row][c] == 1:
            return False

    for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[r][c] == 1:
            return False

    for r, c in zip(range(row, N, 1), range(col, -1, -1)):
        if board[r][c] == 1:
            return False

    return True

def solveNQueens(board, col):
    if col == N:
        printBoard(board)
        return True  

    res = False
    for row in range(N):
        if isSafe(board, row, col):
            board[row][col] = 1 
            res = solveNQueens(board, col + 1) or res 
            board[row][col] = 0  
    return res

board = [[0] * N for _ in range(N)]

if not solveNQueens(board, 0):
    print("No solution found.")
