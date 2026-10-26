class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        res = 0
        stk = []
        
        for i in tokens:
            if i not in ops:
                stk.append(i)
            else:
                if len(stk) <= 1:
                    continue
                elif i == "+":
                    op1= stk.pop()
                    op2 = stk.pop()
                    stk.append(int(op1) + int(op2))
                elif i == "-":
                    op1= stk.pop()
                    op2 = stk.pop()
                    stk.append(int(op2) - int(op1))
                elif i == "*":
                    op1= stk.pop()
                    op2 = stk.pop()
                    stk.append(int(op1) * int(op2))
                else:
                    op1= stk.pop()
                    op2 = stk.pop()
                    stk.append(int(int(op2) / int(op1)))

        return int(stk[0])
