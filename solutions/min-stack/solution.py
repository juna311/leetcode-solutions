class MinStack:

    def __init__(self):
        self.arr = []
    def push(self, value: int):
        l = len(self.arr)

        if l == 0:
            self.arr.append([value, value])
        else:
            prevMin = self.arr[l - 1][1]
            if prevMin > value:
                self.arr.append([value, value])
            else: self.arr.append([value, prevMin])
        

    def pop(self):
        self.arr.pop()

    def top(self):
        l = len(self.arr)
        return self.arr[l-1][0]
   

    def getMin(self):
        l = len(self.arr)

        return self.arr[l - 1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()