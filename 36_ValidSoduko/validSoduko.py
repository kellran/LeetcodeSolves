'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

 

Example 1:

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

 

Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.


'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        return (self.checkRows(board) and
            self.checkColumns(board) and
            self.checkSubBoxes(board))

    def checkRows(self, board):
        for i in range(0, 9):
            checkRows = []
            for j in range(0, 9):

                if board[i][j] not in checkRows or board[i][j] == ".":
                    checkRows.append(board[i][j])
                else:
                    return False
        return True
        

    def checkColumns(self, board):
        # Transpose board
        # https://www.geeksforgeeks.org/python-transpose-elements-of-two-dimensional-list/
        boardTransposed = []
        for i in range(9):
            row =[]
            for item in board:
                # appending to new list with values and index positions
                # i contains index position and item contains values
                row.append(item[i])
            boardTransposed.append(row)
        
        for i in range(0, 9):
            checkRows = []
            for j in range(0, 9):
                if boardTransposed[i][j] not in checkRows or boardTransposed[i][j] == ".":
                    checkRows.append(boardTransposed[i][j])
                else:
                    return False
        return True

    def checkSubBoxes(self, board):
        boxDict = {key: [] for key in range(1, 10)}
        for i in range(0, 9):
            for j in range(0, 9):
                
                # 1
                if i in range(0,3) and j in range (0,3):
                    boxDict[1].append(board[i][j])
                # 2
                elif i in range(0,3) and j in range (3,6):
                    boxDict[2].append(board[i][j])
                # 3
                elif i in range(0,3) and j in range (6,9):
                    boxDict[3].append(board[i][j])

                # 4
                if i in range(3,6) and j in range (0,3):
                    boxDict[4].append(board[i][j])
                # 5
                elif i in range(3,6) and j in range (3,6):
                    boxDict[5].append(board[i][j])
                # 6
                elif i in range(3,6) and j in range (6,9):
                    boxDict[6].append(board[i][j])

                # 7
                if i in range(6,9) and j in range (0,3):
                    boxDict[7].append(board[i][j])
                # 8
                elif i in range(6,9) and j in range (3,6):
                    boxDict[8].append(board[i][j])
                # 9
                elif i in range(6,9) and j in range (6,9):
                    boxDict[9].append(board[i][j])

    
        for key, values in boxDict.items():
            seen = set()
            for value in values:
                if value in seen and value != ".":
                    return False
                seen.add(value)

        return True

 
# It gets it done, but time-wise it's terrible, now time to check out optimal method!
board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]

x = Solution
print(x.isValidSudoku(x,board))