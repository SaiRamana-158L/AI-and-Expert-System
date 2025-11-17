def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(board, row, n):
    if row == n:
        print(board)
        return True
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve(board, row+1, n):
                return True
    return False

n = 8
board = [-1]*n
solve(board, 0, n)
