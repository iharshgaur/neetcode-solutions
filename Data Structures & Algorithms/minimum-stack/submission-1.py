class MinStack:

    def __init__(self):
        self.stack = []
        self.prevMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = min(val, self.prevMin[-1]) if self.prevMin else val
        self.prevMin.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.prevMin.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.prevMin[-1]