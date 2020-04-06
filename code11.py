# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number==0:
            return 0
        if number==1:
            return 1
        A = [1, 2]
        for i in range(3,number+1):
            tmp=A[0]+A[1]
            A[0]=A[1]
            A[1]=tmp
        return A[1]

S=Solution()
number=int(input('请输入台阶数n:'))
print(S.jumpFloor(number))