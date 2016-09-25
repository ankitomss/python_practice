class Solution(object):
    def solveSudoku(self, board):
        if not board or len(board)==0:
            return
        self.solve(board)

        
def solve(self,board):
    for row in xrange(9):
        for col in xrange(9):
            if board[row][col]=='.':
                for c in ['1','2','3','4','5','6','7','8','9']:
                    if self.unvalid(board,row,col,c):
                        board[row][col]=c
                        if self.solve(board):
                            return True
                        else:
                            board[row][col]='.'
                return False
    return True


def unvalid(self,board,i,j,c):
    for row in xrange(9):
        if board[row][j]==c:
            return False
    for col in xrange(9):
        if board[i][col]==c:
            return False
    for row in xrange((i/3)*3,(i/3)*3+3):
        for col in xrange((j/3)*3,(j/3)*3+3):
            if board[row][col]==c:
                return False
    return True