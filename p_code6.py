# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
# 假设压入栈的所有数字均不相等。
# 例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
# 但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        n=len(pushV)
        if not pushV or n!=len(popV):
            return False
        list =[]
        for i in pushV:
            list.append(i)
            while len(list) and list[-1]==popV[0]:
                list.pop()
                popV.pop(0)
        if len(list)!=0:
            return False
        return True

S=Solution()
push1=[1,2,3,4,5]
pop1=[4,3,5,1,2]
print(S.IsPopOrder(push1,pop1))
# list=[]
# for i in range(3,6):
#     list.append(i)
# print(list)