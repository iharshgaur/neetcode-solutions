class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        stk = []

        for i in range(len(temperatures)-1, -1, -1):
            if len(stk) == 0:
                res.append(0)
                stk.append([temperatures[i], i])
            else:
                if temperatures[i] < stk[-1][0]:
                    res.append(stk[-1][1] - i) # index of the top of stack - index of the current temperature
                    stk.append([temperatures[i], i])
                else:
                    while len(stk) > 0 and temperatures[i] >= stk[-1][0]:
                        stk.pop()
                    if len(stk) == 0:
                        res.append(0)
                    else:
                        res.append(stk[-1][1] - i) # index of the top of stack - index of the current temperature
                    stk.append([temperatures[i], i])

        return res[::-1]