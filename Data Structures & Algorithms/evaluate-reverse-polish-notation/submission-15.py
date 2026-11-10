class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            if token in "+-*/":
                v1 = stk.pop()
                v2 = stk.pop()
            if token == "+":
                stk.append(v1 + v2)
            elif token == "-":
                stk.append(v2 - v1)
            elif token == "*":
                stk.append(v1 * v2)
            elif token == "/":
                stk.append(int(v2 / v1))
            else:
                stk.append(int(token))
        return stk[0]