def NQueens(n):
    sol=[]

    def printBoard(board):
        return [''.join(row) for row in board]
    def backtrack(row, cols, diag1, diag2, board):
        if row==n:
            sol.append(printBoard(board))
            return    
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board[row][col]='Q'
            backtrack(row + 1, cols, diag1, diag2, board)
            board[row][col]='.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
    board=[['.' for _ in range(n)] for _ in range(n)]
    cols=set()
    diag1=set() 
    diag2=set() 
  
    backtrack(0,cols ,diag1 ,diag2 ,board)
    return sol

n=4
sol=NQueens(n)
print(f"Total solutions for {n}-Queens: {len(sol)}")
for sol in sol:
    for row in sol:
        print(row)
    print()
