class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        matrix = [[set() for _ in range(3)] for _ in range(3)]
        isValid = True

        for i in range(0, 9):
            for j in range(0, 9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in rows[i]:
                    return False
                if val in cols[j]:
                    return False
                if val in matrix[i // 3][j // 3]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                matrix[i // 3][j // 3].add(val)

        return isValid