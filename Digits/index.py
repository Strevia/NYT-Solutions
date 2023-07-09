from heapq import heappop


class Operations:
    def __init__(self, previousOperation = None):
        self.nums = []
        if previousOperation:
            self.nums = previousOperation.nums
        self.ops = []
        if previousOperation:
            self.ops = previousOperation.ops
    
    def performOp(self, opcode, num1, num2):
        if opcode == 0:
            self.nums.append(self.nums[num1] + self.nums[num2])
        if opcode == 1:
            if self.nums[num1] - self.nums[num2] < 0:
                return
            self.nums.append(self.nums[num1] - self.nums[num2])
        if opcode == 2:
            self.nums.append(self.nums[num1] * self.nums[num2])
        if opcode == 3:
            if self.nums[num1] % self.nums[num2] != 0:
                return
            self.nums.append(self.nums[num1] // self.nums[num2])
        self.ops.append((opcode, num1, num2))
        for ele in sorted([num1, num2], reverse = True):
            del self.nums[ele]
nums = []
nums.append(int(input('Enter number 1: ')))
nums.append(int(input('Enter number 2: ')))
nums.append(int(input('Enter number 3: ')))
nums.append(int(input('Enter number 4: ')))
nums.append(int(input('Enter number 5: ')))
nums.append(int(input('Enter number 6: ')))
target = int(input('Enter target: '))

checking = [nums]
while len(checking) > 0:
    toCheck = checking.pop()
