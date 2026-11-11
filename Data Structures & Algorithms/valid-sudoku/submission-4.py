class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use hash set for rows, cols first. 
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)

        # For the key of the square, we can devide the index of rows and cols by 3
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # if the current place is empty, skip it
                    continue
                
                # check the validation (If it is duplicate (such as in the rows, in the cols, or in the squares)) -> return false
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True

                