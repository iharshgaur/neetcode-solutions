class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        def build(pattern, n, opened, closed):
            print (pattern, n , opened, closed)
            if opened == closed == n:
                res.add(pattern)
            if opened < n:
                build(pattern + "(", n, opened + 1, closed)
            if closed < opened:
                build(pattern + ")", n, opened, closed + 1)

            
        build("", n, 0, 0)
        return list(res)

            
