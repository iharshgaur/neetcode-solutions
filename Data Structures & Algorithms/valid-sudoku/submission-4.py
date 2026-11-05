class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        unit = [[set() for _ in range(3)] for _ in range(3)]

        for r in range (0, len(board)):
            for c in range(0, len(board[r])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r]:
                    return False
                if board[r][c] in cols[c]:
                    return False
                if board[r][c] in unit[r//3][c//3]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                unit[r//3][c//3].add(board[r][c])
        return True