import collections
def solveSudoku( board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """

    def solve(board, i, j, m, n, rows, col, square):

        if j == n:
            i, j = i+1, 0

        if i == m: return True

        if board[i][j] == ".":
            for k in range(1, 10):
                if k not in rows[i] and k not in col[j] and k not in square[(i/3)*3+j/3]:

                    board[i][j] = str(k)
                    rows[i].add(k)
                    col[j].add(k)
                    square[(i/3)*3+j/3].add(k)
                    if solve(board, i , j+1, m, n, rows, col, square):
                        return True
                    square[(i/3)*3+j/3].discard(k)
                    col[j].discard(k)
                    rows[i].discard(k)
                    board[i][j] = "."
        else:
            return solve(board, i, j+1, m, n, rows, col, square)

        return False


    rows = collections.defaultdict(set)
    col = collections.defaultdict(set)
    square = collections.defaultdict(set)


    m, n = len(board), len(board[0])
    for i in range(m):
        print board[i]
        for j in range(n):
            if board[i][j] is not ".":
                c = int(board[i][j])
                rows[i].add(c)
                col[j].add(c)
                square[(i/3)*3+j/3].add(c)

    print rows
    print col
    print square
    solve(board, 0, 0, m, n, rows, col, square)



board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
new = []
for row in board:
    line = []
    for c in row:
        line.append(c)

    new.append(line)

solveSudoku(new)
print new
