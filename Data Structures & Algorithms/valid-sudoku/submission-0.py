class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we only need to do 3 passes
        # linear scan 3 times so only O(n*m) length of sudoku for n sized sudoku
        for i in range(9):
            seen = {}
            row = board[i]
            for item in row:
                if item != '.' and item in seen:
                    return False
                if item != '.':
                    seen[item] = True
            
            # scan for col
            seen = {}
            for j in range(9):
                curr = board[j][i] # scan by col and keep row index constitant
                if curr != '.' and curr in seen:
                    return False
                if curr != '.':
                    seen[curr] = True
            
            # check 3x3
            # ig i=0-3
            seen = {}
            row_start = (i % 3) * 3
            col_start = (i // 3) * 3
            for j in range(row_start, row_start + 3):
                for k in range(col_start, col_start + 3):
                    curr = board[j][k] # scan by col and keep row index constitant
                    if curr != '.' and curr in seen:
                        return False
                    if curr != '.':
                        seen[curr] = True

        return True