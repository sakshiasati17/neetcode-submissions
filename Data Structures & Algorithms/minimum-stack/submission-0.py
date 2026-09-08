class MinStack:

    def __init__(self):
        self.stackk=[]
    def push(self, val: int) -> None:
        self.stackk.append(val)
        

    def pop(self) -> None:
        self.stackk.pop()
        

    def top(self) -> int:
        return self.stackk[-1]

        

    def getMin(self) -> int:
        
        return min(self.stackk)
        
