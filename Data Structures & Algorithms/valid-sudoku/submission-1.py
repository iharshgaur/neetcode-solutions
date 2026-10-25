class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                # 2. build the box key
                key = (r // 3, c // 3)
                # 3. if v is in any of the three groups: return False

                if v in rows[r] or v in cols[c] or v in boxes[key]:
                    return False

                # 4. add v to all three groups

                rows[r].add(v)
                cols[c].add(v)
                boxes[key].add(v)
        return True