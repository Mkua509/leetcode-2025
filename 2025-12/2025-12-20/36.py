class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # Check for Row
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])


        # Check for Col
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[col][i] == ".":
                    continue
                if board[col][i] in seen:
                    return False
                seen.add(board[col][i])

        # For Square
        for square in range(9):
            seen = set()
