class Solution:
    # 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
    # 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，
    # 超过数组长度的一半，因此输出2。如果不存在则输出0。
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        numbers.sort()
        i=0
        mid=numbers[len(numbers)//2]
        for j in numbers:
            if j==mid:
                i=i+1
            if i>=(len(numbers)//2+1):
                return mid
        return 0
#求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
#题解思路：短路求值原理。使用逻辑and（与）或者逻辑or（或），如果出现0则逻辑符号后面的语句不会再执行。
    def Sum_Solution(self, n):
        sum=n
        return (n>0) and (sum+self.Sum_Solution(n-1))

S=Solution()
numbers=eval(input())
# out=S.MoreThanHalfNum_Solution(numbers)
out=S.Sum_Solution(numbers)
print(out)

# a=[1,3,5,2,6,6,6,6,7,4]
# a.sort()
# print(a)