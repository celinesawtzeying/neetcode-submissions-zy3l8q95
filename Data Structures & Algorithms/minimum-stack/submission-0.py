class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack = self.stack[:-1]  

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min_int = float("inf")
        for x in self.stack:
            min_int = min(min_int,x)
        return min_int

        
