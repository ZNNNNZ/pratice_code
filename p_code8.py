'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
栈是先进后出，队列是先进先出，所以用两个栈来实现队列的push和pop操作
'''
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.stack3 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
        # self.stack1=node
    def pop(self):
        # return xx
        if self.stack2 == []:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
"""
    def push(self, node):
        self.stack1=node
    def pop(self):
        # return xx
        if self.stack2 == []:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        while self.stack2:
            self.stack3.append(self.stack2.pop())
        return self.stack3
"""
node=list(eval(input('请输入队列：')))
# node=[1,2,3]
S=Solution()
S.push(node)
print(S.pop())