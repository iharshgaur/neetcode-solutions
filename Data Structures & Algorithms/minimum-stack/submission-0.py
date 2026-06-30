import math

class MinStack:

    def __init__(self):
        self.min_num = [math.inf]
        self.items = []
        

    def push(self, val: int) -> None:
        self.min_num.append(min(self.min_num[-1], val))
        self.items.append(val)


        

    def pop(self) -> None:
        if not len(self.items) == 0:
            self.items.pop()
            self.min_num.pop()
        else:
            raise IndexError("Pop from empty stack")
        
        

    def top(self) -> int:
        if not len(self.items) == 0:
            return self.items[-1]
        

    def getMin(self) -> int:
        return self.min_num[-1]