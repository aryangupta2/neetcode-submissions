class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:

        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        
        removed_val = self.stack.pop()

        if len(self.min_stack) > 0:
            if removed_val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:

        if len(self.stack) == 0:
            return None

        return self.stack[-1]

    def getMin(self) -> int:

        if len(self.min_stack) == 0:
            return None
        
        return self.min_stack[-1]


        
