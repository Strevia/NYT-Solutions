OPS = ['+', '-', '*', '/']

class Operations:
    def __init__(self, previousOperation = None):
        self.nums = []
        if previousOperation:
            self.nums = list(previousOperation.nums)
        self.ops = []
        if previousOperation:
            self.ops = list(previousOperation.ops)
    
    def performOp(self, opcode, num1, num2):
        if opcode == 0:
            self.nums.append(self.nums[num1] + self.nums[num2])
        if opcode == 1:
            if self.nums[num1] - self.nums[num2] < 0:
                return False
            self.nums.append(self.nums[num1] - self.nums[num2])
        if opcode == 2:
            self.nums.append(self.nums[num1] * self.nums[num2])
        if opcode == 3:
            if self.nums[num2] == 0 or self.nums[num1] % self.nums[num2] != 0:
                return False
            self.nums.append(self.nums[num1] // self.nums[num2])
        self.ops.append(f"{self.nums[num1]} {OPS[opcode]} {self.nums[num2]} = {self.nums[-1]}")
        for ele in sorted([num1, num2], reverse = True):
            del self.nums[ele]
        return True
nums = []
nums.append(int(input('Enter number 1: ')))
nums.append(int(input('Enter number 2: ')))
nums.append(int(input('Enter number 3: ')))
nums.append(int(input('Enter number 4: ')))
nums.append(int(input('Enter number 5: ')))
nums.append(int(input('Enter number 6: ')))
target = int(input('Enter target: '))

starting = Operations()
starting.nums = nums
checking = [starting]
while len(checking) > 0:
    toCheck = checking.pop(0)
    for i in range(len(toCheck.nums)):
        for j in range(len(toCheck.nums)):
            if i == j:
                continue
            for op in range(4):
                newOp = Operations(toCheck)
                if newOp.performOp(op, i, j):
                    if target in newOp.nums:
                        for operation in newOp.ops:
                            print(operation)
                        exit()
                    if len(newOp.nums) > 1:
                        checking.append(newOp)
