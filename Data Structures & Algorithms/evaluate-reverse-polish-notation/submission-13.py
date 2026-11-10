class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            if token == "+":
                v1 = stk.pop()
                v2 = stk.pop()
                stk.append(v1 + v2)
            elif token == "-":
                v1 = stk.pop()
                v2 = stk.pop()
                stk.append(v2 - v1)
            elif token == "*":
                v1 = stk.pop()
                v2 = stk.pop()
                stk.append(v1 * v2)
            elif token == "/":
                v1 = stk.pop()
                v2 = stk.pop()
                stk.append(int(v2 / v1))
            else:
                stk.append(int(token))
        return stk[0]