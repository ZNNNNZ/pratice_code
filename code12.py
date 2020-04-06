#jumpFloorII函数，题目要求——一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法。
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number<=0:
            return 0
        a0=1
        for i in range(2,number+1):
            a0=a0*2
        return a0
#rectCover函数题目要求——我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
# 比如n=3时，2*3的矩形块有3种覆盖方法：
    def rectCover(self, number):
        # write code here
        if number <= 0:
            return 0
        if number > 0 and number <= 2:
            return number
        a0 = 2
        a1 = 3
        for i in range(4, number + 1):
            tmp = a0 + a1
            a0 = a1
            a1 = tmp
        return a1
#输入一个数，输出其二进制中1的个数。若是负数，则使用补码形式。
    def NumberOf1(self, n):
        # write code here
        num=0
        if n<0:
            n=n&0xffffffff #这里是把负数转变为了和它二进制补码一样形式的正数
        while n:    #如果是负数，以0为终止条件会陷入死循环，因为python没有溢出限制
            num=num+1
            # m1=bin(n&0xffffffff)
            # m2=bin((n-1)&0xffffffff)
            n=n&(n-1)
            # m3=bin(n&0xffffffff)
        return num


S=Solution()
number=int(input('请输入青蛙跳的台阶数：'))
print(S.jumpFloorII(number))
# print(S.rectCover(number))
# print(S.NumberOf1(-15))